from datetime import datetime
import os
import sys

# Add root to path for utility access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.notify import send_telegram_message

print("🔍 ClawMentor Bharat - Opportunity Tracker")
print("="*65)
print(f"📅 {datetime.now().strftime('%d %B %Y')}\n")

alerts = (
    "🌟 **New Opportunities Detected!**\n\n"
    "1. **Samsung PRISM Internship**\n"
    "2. **Google Summer of Code 2026**\n"
    "3. **Microsoft Engage**"
)

print(alerts)

# Send Proactive Alert
send_telegram_message(alerts)

print("\nWould you like me to track specific companies or domains (AI/ML, SDE, etc.)?")
