from flask import Flask, request
import json

app = Flask(__name__)

# Load businesses from services.json
with open("services.json", "r") as f:
    services = json.load(f)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.form.get("Body", "").lower()
    matched = []

    # Match message with any business type
    for s in services:
        if s["type"].lower() in incoming_msg:
            matched.append(s)

    if not matched:
        return "No matching services found. Try something like: 'I need a plumber'"

    # Show sponsored listings first
    matched.sort(key=lambda x: not x.get("sponsored", False))

    # Build response
    result = "Here are some options:\n"
    for s in matched:
        result += f"\n📌 {s['name']} ({s['type']})\n"
        result += f"📞 {s['phone']}\n"
        result += f"📍 {s['location']}\n"
        result += f"📝 {s['note']}\n"
        
        if "email" in s:
            result += f"✉️ {s['email']}\n"
        if "website" in s:
            result += f"🌐 {s['website']}\n"
        if "hours" in s:
            result += f"🕒 {s['hours']}\n"

    return result.strip()

if __name__ == "__main__":
    app.run(debug=True)