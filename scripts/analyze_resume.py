import fitz  # PyMuPDF
import os
import sys

# Add root to path for utility access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.llm import generate_ai_response

def analyze(resume_path, target_role):
    # 1. Extract Text
    if not os.path.exists(resume_path):
        return f"Error: Resume file not found at {resume_path}"
        
    doc = fitz.open(resume_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # 2. Call Groq API for analysis
    prompt = (
        f"Analyze this parsed resume text against standard requirements for a {target_role} "
        f"and identify 2-3 missing technical skills. Return ONLY a comma-separated list of the missing skills. "
        f"Resume text: {text[:2000]}"
    )
    
    ai_output = generate_ai_response(prompt)
    gaps = [g.strip() for g in ai_output.split(',') if g.strip()]
    if not gaps:
        gaps = ["Error detecting gaps from AI."]

    # 3. Update Durable Memory (ROADMAP.md)
    # The memory folder is typically relative to the workspace root
    memory_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "memory", "ROADMAP.md")
    
    with open(memory_path, "a") as f:
        f.write(f"\n## New Gaps Detected via Resume Analysis for {target_role}\n")
        for gap in gaps:
            f.write(f"* [ ] {gap}\n")

    return f"Analysis complete for {target_role}. Roadmap updated."

if __name__ == "__main__":
    # Example usage for testing
    # result = analyze("resume.pdf", "AI Engineer")
    # print(result)
    pass
