# 📸 Instagram Automation using Selenium + Cookies

This project automates login, search, follow, and profile data extraction on Instagram using **Python Selenium** and **cookie-based login**.

---

## 🚀 Features

- ✅ Manual login only once — then reused via cookies
- 🔍 Searches and opens any Instagram profile (`@cbitosc`)
- 🤝 Follows the account (if not already followed)
- 📄 Extracts profile info: Posts, Followers, Following, Bio
- 💾 Saves data to `cbitosc_profile.txt`
- 🧠 Handles Instagram's UI updates better than older scripts

---

## 📁 Folder Structure

```
instagram_automation_cookie_login/
├── automate_insta.py         # Main automation script
├── save_cookies.py           # Run once to log in and save cookies
├── insta_cookies.pkl         # [Generated] Instagram login cookies
├── cbitosc_profile.txt       # [Generated] Extracted profile data
├── login_status.png          # [Generated] Screenshot during cookie save
├── requirements.txt          # Required packages
└── README.md                 # This file
```

---

## 🛠 Requirements

- Python 3.8+
- Google Chrome (latest)
- ChromeDriver (managed automatically)

### 🔧 Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 Step-by-Step Instructions

### 🔐 Step 1: Save Instagram Login Session
Run once and log in manually when the browser opens.

```bash
python save_cookies.py
```

➡️ After logging in and reaching your feed, return to the terminal and press **Enter**.

This will generate:
- `insta_cookies.pkl` — your saved login
- `login_status.png` — visual confirmation

---

### 🤖 Step 2: Automate Profile Tasks
This script:
- Logs in using cookies
- Searches for `@cbitosc`
- Follows the account
- Extracts post/follower info

```bash
python automate_insta.py
```

✅ Output saved in `cbitosc_profile.txt`

---

## 📌 Notes

- Works best with **dummy/test accounts**.
- Instagram UI changes frequently — use latest Chrome.
- This project is for educational purposes only.

---

## 🧠 Credits

Built by [Your Name]  
Powered by: Selenium, WebDriver Manager

MIT License
