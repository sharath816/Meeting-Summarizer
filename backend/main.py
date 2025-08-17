import os
import logging
import smtplib
from email.message import EmailMessage
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("summarizer")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI(title="Meeting Notes Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    transcript: str
    prompt: Optional[str] = "Summarize the meeting. Provide bullets and action items."
    model: Optional[str] = "gemini-2.5-flash"

class EmailRequest(BaseModel):
    from_email: EmailStr
    to_emails: List[EmailStr]
    subject: str
    summary: str

@app.post("/generate")
async def generate(req: GenerateRequest):
    """Generate summary using Gemini."""
    try:
        contents = f"Instruction: {req.prompt}\n\nTranscript:\n{req.transcript}"

        model = genai.GenerativeModel(req.model)
        response = model.generate_content(contents)

        text = getattr(response, "text", None)
        if text is None:
            text = str(response)

        return {"summary": text}

    except Exception as e:
        logger.exception("Generation failed")
        return {"error": str(e)}

@app.post("/send-email")
async def send_email(req: EmailRequest):
    """Send email via SMTP using .env credentials."""
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")

    if not smtp_host or not smtp_user or not smtp_pass:
        return {"error": "SMTP not configured. Set SMTP_* env vars in .env"}

    msg = EmailMessage()
    msg["From"] = req.from_email
    msg["To"] = ", ".join(req.to_emails)
    msg["Subject"] = req.subject
    msg.set_content(req.summary)   

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        return {"ok": True}
    except Exception as e:
        logger.exception("Failed to send email")
        return {"error": str(e)}

