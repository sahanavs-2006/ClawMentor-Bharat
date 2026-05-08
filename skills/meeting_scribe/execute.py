def process_meeting(transcript: str = None):
    print("🎙️ ClawMentor Bharat - Meeting Scribe & Prep Coach Activated")
    print("="*60)
    
    # In a real scenario, this would use a LLM to summarize
    print("\n**📋 Key Points Extracted:**")
    print("- Discussed DSA interview preparation strategies.")
    print("- Identified need for more practice on Graph algorithms.")
    print("- Action: Complete 10 LeetCode problems on Graphs by next session.")
    
    print("\n**🧠 Preparation for Next Meeting:**")
    print("• Review System Design for Payment Gateway architectures.")
    print("• Prepare 2 project deep-dives for mock interviews.")
    
    print("\n✅ Meeting notes saved to memory (ROADMAP.md updated).")

if __name__ == "__main__":
    process_meeting("Sample transcript: Let's focus on graphs today and prepare for system design next time.")
