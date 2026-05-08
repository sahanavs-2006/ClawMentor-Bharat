---
name: resume_gap_analyzer
description: Parses an engineering resume to identify skill gaps against industry-standard roles like AI Engineer or SDE.
parameters:
  resume_path: string
  target_role: string

python:
  script: scripts/analyze_resume.py
---

# Instructions

1. Use the PyMuPDF library to extract raw text from the PDF at {{resume_path}}.
2. Identify the student's current technical stack (languages, frameworks, tools).
3. Compare the findings against the requirements for {{target_role}}.
4. Output a "Gap Report" identifying exactly what the student is missing.
5. Update the agent's Durable Memory by appending these gaps to ROADMAP.md.

## Tool Mapping
- **Python**: `scripts/analyze_resume.py`
