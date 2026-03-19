import anthropic
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

ANTHROPIC_API_KEY  = os.environ["ANTHROPIC_API_KEY"]
GMAIL_ADDRESS      = os.environ["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
RECIPIENT_EMAIL    = os.environ.get("RECIPIENT_EMAIL", GMAIL_ADDRESS)

FOCUS_AREAS = """
- Startup and VC funding rounds
- Nonprofit fundraising
- Agriculture financing and agri-tech investment
- Gender equity funding (SDG 5)
- Decent work and economic growth investments (SDG 8)
- Reduced inequalities funding (SDG 10)
- Responsible consumption and production (SDG 12)
- Climate finance
"""

def generate_digest():
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    today = date.today().strftime("%B %d, %Y")

    prompt = f"""Today is {today}. Search the web and find 4-5 recent fundraising news items.

Focus areas:
{FOCUS_AREAS}

Write a short HTML email with:
- A heading showing the date
- 4-5 news items, each with a bold title and 1 sentence summary
- Simple inline CSS (font-family: Arial; max-width: 600px; margin: auto)

Format as:
SUBJECT: Daily Fundraising Digest - {today}
---
<html content here>"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    full_text = ""
    for block in response.content:
        if hasattr(block, "text"):
            full_text += block.text

    if "SUBJECT:" in full_text and "---" in full_text:
        parts = full_text.split("---", 1)
        subject = parts[0].replace("SUBJECT:", "").strip()
        body = parts[1].strip()
    else:
        subject = f"Daily Fundraising Digest — {today}"
        body = full_text

    return subject, body

def send_email(subject, html_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = GMAIL_ADDRESS
    msg["To"]      = RECIPIENT_EMAIL
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

    print(f"Digest sent to {RECIPIENT_EMAIL}")

if __name__ == "__main__":
    print("Fetching today's fundraising news...")
    subject, body = generate_digest()
    print(f"Subject: {subject}")
    print("Sending email...")
    send_email(subject, body)
