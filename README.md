# InfoBot-Parys — WhatsApp Local Business Search Bot

## 🧠 Overview

**InfoBot-Parys** is a WhatsApp chatbot that helps locals in Parys, South Africa, find nearby services like plumbers, tutors, hairdressers, and more.

- Written in Python using the free WhatsApp API (Twilio Sandbox)
- Simple, human-editable business listings file
- Built entirely on a phone — no laptop required!


## 📁 Project Structure

```
parys-whatsapp-bot/
├── app.py                # Main bot logic
├── services.txt          # Editable, human-friendly business listings
├── services.json         # Bot-readable data (auto-generated)
├── requirements.txt      # Python dependencies
├.txt             # Setup & developer instructions
├── magic-tool/           # Utility scripts for verification, conversion, backups
├── backups/              # Auto backups of JSON data
├── versioning/           # Manual labeled snapshots of data
├── logs/                 # Logs from data build processes
```


## ⚙️ Setup & Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```


### 2. Add or Edit Business Listings

Open `services.txt` and add business info like:

```
type: plumber
name: Tumahole Pipes
phone: 0812345678
location: Tumahole
note: 24/7 emergency plumbing
sponsored: no
```

- Set `sponsored: yes` for a business to show at the top of search results.

### 3. Build the Data File

**Change directory into the tools folder:**
```bash
cd magic-tool
```

**Run the build script:**
```bash
bash make.sh
```


- This will:
  - Verify your listings for missing fields
  - Backup the current `services.json`
  - Convert `services.txt` to `services.json`
  - Save a detailed log in `logs/`
- **If verification fails, fix errors in `services.txt` and run again.**

---

### 4. Run the Bot Locally

**From the root folder:**
```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```


### 5. Connect to WhatsApp via Twilio Sandbox

- Sign up and activate the WhatsApp Sandbox at [twilio.com/whatsapp](https://www.twilio.com/whatsapp)
- From your phone, send the join code to the sandbox number

**Set your webhook URL in the Twilio console to your deployment URL (example):**
```
https://your-deployment-url.com/whatsapp
```



### 6. Test Your Bot

Try sending WhatsApp messages like:

```
I need a plumber
```
```
Find me a tutor
```
```
Bakery in Tumahole
```

Your bot should reply```

**Save a labeled snapshot:**
```bash
bash save-version.sh
```

**Trigger Netlify rebuild (if used):**
```bash
bash auto-ping.sh
```

**Notify bot of updates:**
```bash
bash auto-ping-Telegram-Whatsapp.sh
```

**Convert TXT to JSON:**
```bash
python txt_to_json.py
```

**Convert JSON to TXT:**
```bash
python json_to_txt.py
```



## 🗂 Logs & Versioning

- Every run of `make.sh` creates a timestamped log file in `logs/`
- Backups and manual snapshots help you restore previous working states



## 💡 Tips & Notes

- **Edit only `services.txt`** — don’t change `services.json` directly.
- Use short category names (plumber, baker, tutor, salon, etc.).
- Sponsored listings (`sponsored: yes`) show first in results.
- Expand the bot to cover nearby towns by adding more listings.
- Use logs to troubleshoot build or data issues.



## ❤️ Built For Real People

This bot was built without a laptop, while cooking noodles, using just a phone.  
Fork, remix, or rebuild for your own town or community!  
Every update helps your community get better connected.  
Keep building — one bot at a time. 💻🔥



## 📅 Date Built

**June 18, 2025**


Feel free to open issues or submit pull requests for improvements.  
Thank you for using InfoBot-Parys! 🚀

