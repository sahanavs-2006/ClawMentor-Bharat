import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_telegram(message: str, chat_id: str = None):
    """Send message via Telegram"""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    target_chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not target_chat_id:
        print("⚠️ Telegram credentials not configured. Skipping.")
        return False
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": target_chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"📤 Telegram sent: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Telegram failed: {e}")
        return False

def send_whatsapp(message: str, to_number: str = None):
    """Send via Twilio WhatsApp"""
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
    target_number = to_number or os.getenv("USER_WHATSAPP_NUMBER")
    
    if not sid or not token or not from_number or not target_number:
        print("⚠️ Twilio credentials not configured. Skipping WhatsApp.")
        return False
        
    try:
        from twilio.rest import Client
        client = Client(sid, token)
        
        # Ensure numbers are in WhatsApp format
        msg = client.messages.create(
            from_=f"whatsapp:{from_number}",
            body=message,
            to=f"whatsapp:{target_number}"
        )
        print(f"📤 WhatsApp sent via Twilio: {msg.sid}")
        return True
    except Exception as e:
        print(f"❌ WhatsApp failed: {e}")
        return False

def notify_user(message: str, channel: str = "telegram"):
    """Multiplexed notification utility"""
    if channel == "telegram":
        return send_telegram(message)
    elif channel == "whatsapp":
        return send_whatsapp(message)
    return False

if __name__ == "__main__":
    print("🧪 Running multi-channel notification test...")
    notify_user("🤖 **ClawMentor Bharat System Check**\nTelegram is correctly configured.", "telegram")
    notify_user("🤖 *ClawMentor Bharat System Check*\nWhatsApp is correctly configured.", "whatsapp")
