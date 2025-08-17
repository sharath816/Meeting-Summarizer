# 🤖 AI Meeting Summarizer

The **AI Meeting Summarizer** is a web application that allows users to quickly generate concise summaries of meeting transcripts using Google’s Gemini AI. Users can also share the generated summaries via email with a single click. The system focuses on efficiency, usability, and clean UX/UI design.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Core Modules](#core-modules)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

Meetings often generate long transcripts that are tedious to read. This application solves that problem by:

1. Allowing users to **paste or upload meeting transcripts**.
2. Generating a **structured summary** with action items and bullet points using Google Gemini.
3. Allowing users to **copy or share the summary via email** directly.
4. Providing a **clean, modern, mobile-friendly UI** with responsive interactions.

The system is designed for quick understanding of meeting outcomes without reading the full transcript.

---

## Features

- **Transcript Input**
  - Paste raw meeting notes or transcripts.
  - Optional custom instruction/prompt to guide the AI summary.
  
- **AI-Powered Summary**
  - Uses **Google Gemini** to generate accurate summaries.
  - Returns actionable insights, bullet points, and highlights key discussion items.

- **Interactive Summary**
  - Copy the summary to clipboard with a single click.
  - Send the summary via email directly (sender, receiver, subject configurable).

- **Responsive UI**
  - Mobile-friendly design using **Tailwind CSS**.
  - Loading indicators during generation and email sending.
  - Success animations for user feedback.

- **Security & Validation**
  - Input validation for email addresses.
  - Optional prompt for custom AI instructions.
  - Backend securely communicates with AI API using environment variables.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend | HTML5, Tailwind CSS, Vanilla JS | Clean, responsive, interactive UI |
| Backend | Python 3, FastAPI | REST API endpoints for AI summary & email |
| AI | Google Gemini (Generative AI) | Text summarization and actionable insights |
| Email | SMTP (via `smtplib`) | Sending summaries to recipients |
| Environment | `python-dotenv` | Secure storage of API keys and SMTP credentials |

---

## Architecture

Frontend (HTML + Tailwind CSS + JS)
|
|--- Fetch API calls
|
Backend (FastAPI)
|--- /generate endpoint (calls Gemini API)
|--- /send-email endpoint (SMTP integration)

- **Frontend**: Handles user input, displays summaries, shows loaders and animations.
- **Backend**: Receives transcript and prompt, calls Gemini AI, returns structured summary.
- **Email Service**: Sends the summary to specified recipients via SMTP.

---

## Core Modules

### 1. Transcript Summarizer
- **Endpoint:** `/generate`
- **Input:** Transcript text + optional custom prompt.
- **Process:** Sends the request to Google Gemini API, retrieves structured summary.
- **Output:** JSON with summary text.

### 2. Email Sharing
- **Endpoint:** `/send-email`
- **Input:** Sender email, recipient emails, subject.
- **Process:** Uses SMTP to send the generated summary automatically. No manual copy required.
- **Output:** JSON with success or error message.

### 3. Frontend Interactions
- **Summary Generation:** Shows spinner animation while processing.
- **Email Sending:** Loader during sending; success animation on completion.
- **Copy Summary:** Clipboard API integration for instant copying.

---

## Usage

1. Open the **web application** in a browser.
2. Paste your **meeting transcript** in the input box.
3. Optionally, add a **custom instruction** for the summary.
4. Click **Generate Summary**:
   - Wait for the spinner to finish.
   - View the AI-generated summary below.
5. Copy the summary to clipboard using the **Copy button**.
6. Share via email by opening the **Email card**:
   - Fill in **From, To, Subject**.
   - Click **Send Email**.
   - Success animation will confirm sending.

---

## Screenshots

1. **Transcript Input & Prompt**
![Transcript Input](screenshots/transcript_input.png)

2. **Generated Summary**
![Generated Summary](screenshots/generated_summary.png)

3. **Email Share**
![Email Share](screenshots/email_share.png)

4. **Animations**
![Loading & Success Animations](screenshots/animations.png)

---

## Future Enhancements

- Support **file uploads** (PDF, DOCX) for transcript input.
- **Multi-language** transcript summarization.
- **User accounts** for saving and managing summaries.
- Integration with **calendar apps** to automatically summarize meeting notes.
- **Advanced AI features**: sentiment analysis, action item extraction.

---

## License

This project is licensed under the **MIT License**. See `LICENSE` file for details.

---

## Contact

- **Author:** Sharath M T  
- **Email:** sharath@example.com  
- **GitHub:** [https://github.com/sharath816/Meeting-Summarizer](https://github.com/sharath816/Meeting-Summarizer)

---