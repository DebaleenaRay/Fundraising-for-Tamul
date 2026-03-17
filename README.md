# 📬 Daily Fundraising Digest

Automatically sends a daily email digest of fundraising news — powered by Claude AI + web search, delivered via Gmail, scheduled by GitHub Actions.

**Focus areas:** Startup/VC rounds · Nonprofits · Agriculture · Gender equity · Climate finance · SDGs 5, 8, 10, 12

---

## 🚀 Setup (5 steps)

### 1. Fork or clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/fundraising-digest.git
cd fundraising-digest
```

### 2. Get your API keys

**Anthropic API key**
- Go to [console.anthropic.com](https://console.anthropic.com)
- Create an API key under *API Keys*

**Gmail App Password**
- Go to your Google Account → Security → [2-Step Verification](https://myaccount.google.com/security)
- Make sure 2FA is enabled
- Then go to [App Passwords](https://myaccount.google.com/apppasswords)
- Create a new app password (name it anything, e.g. "Fundraising Digest")
- Copy the 16-character password — you won't see it again

### 3. Add GitHub Secrets
In your GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**

Add these 4 secrets:

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `GMAIL_ADDRESS` | Your Gmail address (e.g. `you@gmail.com`) |
| `GMAIL_APP_PASSWORD` | The 16-char App Password from step 2 |
| `RECIPIENT_EMAIL` | Email to receive the digest (can be same as above) |

### 4. Push to GitHub
```bash
git add .
git commit -m "Initial setup"
git push origin main
```

### 5. Test it manually
- Go to your repo → **Actions** tab
- Click **Daily Fundraising Digest**
- Click **Run workflow** → **Run workflow**
- Watch the logs — you should receive an email within ~60 seconds!

---

## ⏰ Schedule

The digest runs every day at **7:00 AM UTC** by default.

To change the time, edit `.github/workflows/daily_digest.yml`:
```yaml
- cron: '0 7 * * *'   # minute hour * * *
```

**Common timezone conversions:**
| Your time | UTC cron |
|---|---|
| 6 AM EAT (Nairobi) | `0 3 * * *` |
| 7 AM WAT (Lagos) | `0 6 * * *` |
| 8 AM SAST (Joburg) | `0 6 * * *` |
| 9 AM IST | `30 3 * * *` |
| 7 AM GMT | `0 7 * * *` |
| 7 AM EST | `0 12 * * *` |

---

## 📁 File structure

```
fundraising-digest/
├── .github/
│   └── workflows/
│       └── daily_digest.yml   # GitHub Actions schedule
├── send_digest.py             # Main script
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🛠 Customization

To change the focus areas, edit the `FOCUS_AREAS` variable in `send_digest.py`.

To change the recipient, update the `RECIPIENT_EMAIL` secret in GitHub.
# Fundraising-for-Tamul
