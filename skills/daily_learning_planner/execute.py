from datetime import datetime
from pathlib import Path
import os
import sys

# Add root to path for utility access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.notify import notify_user
from utils.llm import generate_ai_response

def main():
    print("🚀 ClawMentor Bharat - Daily Learning Planner")
    print("="*60)
    report_date = datetime.now().strftime('%A, %d %B %Y')
    print(f"📅 {report_date}\n")
    
    prompt = (
        f"You are ClawMentor Bharat, an AI career mentor for Indian engineering students. "
        f"Generate a personalized daily learning plan for today ({report_date}). "
        f"Keep it concise (3-4 bullet points) covering morning, afternoon, and evening. "
        f"Focus on coding, project building, and interview prep. Format it beautifully with emojis."
    )
    
    ai_plan = generate_ai_response(prompt)
    
    plan = f"📅 **Daily Plan: {report_date}**\n\n{ai_plan}"
    
    print(plan)
    
    # Send Proactive Reminder
    notify_user(f"🚀 **ClawMentor Bharat - Today's Plan**\n\n{plan}", "telegram")
    
    print("\nReply with 'done' when you finish tasks!")

if __name__ == "__main__":
    main()
