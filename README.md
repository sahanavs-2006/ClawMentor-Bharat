# ClawMentor Bharat 🦞

**An OpenClaw-Powered Autonomous Career Intelligence Agent for Indian Engineering Students**

![ClawMentor Bharat](https://via.placeholder.com/800x400/0A2540/00BFFF?text=ClawMentor+Bharat)

**Samsung PRISM OpenClaw Hackathon 2026**  
**Team Number**: RVCE_ClawMentors  
**Team Name**: ClawMentors  
**College**: RV College of Engineering, Bengaluru

---

## 🎥 Project Video Demo
**[Insert Link to Project Video Demo Here]** - *(Explaining the solution & Walkthrough)*

## 📊 Project Presentation (PPT)
**[RVCollegeOfEngineering_ClawMentors.pptx](./RVCollegeOfEngineering_ClawMentors.pptx)** - *(Understanding what we have built)*

## 📦 APK / SDK
**N/A** - *(This project is deployed as an OpenClaw Dockerized Agent)*

---

### 🎯 Problem
Engineering students today face **Information Overload**, a **Lack of Structured Career Guidance**, and **No Continuous Personalized Mentorship**. They struggle to identify the right skills and opportunities needed to secure top-tier placements.

### 💡 Solution
ClawMentor Bharat addresses these challenges by acting as a **24/7 Sovereign AI Career Sentinel**. Built on the OpenClaw framework, it proactively guides students from their college desks to top-tier placements by providing personalized daily learning plans, analyzing resume gaps, and offering continuous, data-driven mentorship.

### ✨ Key Features
- **Daily Learning Planner** — Generates realistic, time-blocked plans tailored to student schedules.
- **Resume Gap Analyzer** — Uses PyMuPDF to detect missing technical skills and suggests immediate improvements.
- **Project Recommendation Engine** — Suggests high-impact portfolio projects that specifically target detected skill gaps.
- **Opportunity Tracker** — Proactively monitors ArXiv, GitHub, and hackathon platforms for internship and research alerts.
- **Weekly Progress Digest** — Aggregates weekly performance and research into professional **Microsoft Word (.docx)** summaries.
- **Repository Analyzer & Build Engine** — Analyzes GitHub repos for tech stack and build feasibility.
- **Meeting Scribe & Prep Coach** — Transcribes meetings and generates action items automatically.
- **Proactive Multi-Channel Notifications** — Real-time alerts via **Telegram** and **WhatsApp** for all career events.
- **Persistent Memory** — Utilizes OpenClaw's Durable Memory (`SOUL`, `USER`, `ROADMAP`, `HEARTBEAT`) for cross-session continuity.

---

### 🏗️ System Architecture
ClawMentor Bharat is built on the **OpenClaw 5-Layer Stack**:
1. **Communication Layer**: Integration with Telegram and WhatsApp via Twilio.
2. **Channel Adapter**: Normalizes cross-platform messaging into agent intents.
3. **Gateway Layer**: Orchestrates sessions, memory, and routing.
4. **Pi Engine**: The core reasoning loop for roadmap updates and gap detection.
5. **Skill Execution Layer**: Sandboxed execution of specialized Python modules.

---

### 🚀 Setup & Instructions
```bash
# 1. Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. Start the Gateway
openclaw gateway run

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Deploy ClawMentor Bharat
docker-compose up -d
```

### 🎮 Usage
Once deployed, ClawMentor Bharat runs as an autonomous background agent. 
- **Interact**: Chat with the agent via its configured communication channels (**Telegram** / **WhatsApp**).
- **Profile Initialization**: The agent will read the `memory/USER.md` profile to understand the student's goals and establish an automated `HEARTBEAT.md` scheduler.
- **Track Progress**: Check the `memory/ROADMAP.md` file regularly. The agent continuously updates your personalized career roadmap, skill gaps, and learning milestones here.
- **Continuous Mentorship**: Receive proactive daily alerts for new opportunities, and weekly `.docx` progress summaries directly from the agent.

### 📁 Project Structure
```bash
ClawMentor-Bharat/
├── memory/                    # Durable Cognitive Memory (Markdown-based)
│   ├── SOUL.md                # Persona and core behavioral logic
│   ├── USER.md                # Student profile and career goals
│   ├── ROADMAP.md             # Living progress tracker
│   └── HEARTBEAT.md           # Autonomous task scheduler
├── skills/                    # Specialized Skill execution modules
│   ├── resume_gap_analyzer/
│   ├── daily_learning_planner/
│   ├── project_recommendation/
│   ├── opportunity_tracker/
│   ├── weekly_progress_digest/
│   ├── repo_analyzer/
│   └── meeting_scribe/
├── docker-compose.yml         # Tank-native sovereign deployment config
├── OpenClaw_AI_Disclosure.pdf # Official AI Disclosure document
├── RVCollegeOfEngineering_ClawMentors.pptx  # Hackathon project presentation file
└── README.md
```

### 🛠️ Tech Stack
- **Core Agent**: [OpenClaw Framework](https://openclaw.ai)
- **Languages**: Python (Skills), TypeScript (Gateway)
- **Local Intelligence**: Ollama (Llama 3.2)
- **Libraries**: PyMuPDF, python-docx, twilio, python-dotenv
- **Channels**: Telegram Bot API, Twilio WhatsApp API
- **Infrastructure**: Docker Compose, OpenClaw Tank

---

### 🤖 AI Disclosure
**[OpenClaw_AI_Disclosure.pdf](./OpenClaw_AI_Disclosure.pdf)** - *(Official AI utilization and compliance disclosure)*

This project was developed with the assistance of the following AI models and tools:
- **Local Intelligence (Ollama / Llama 3.2)**: Used to power the core reasoning engine, gap detection, and learning plan generation within the OpenClaw environment.
- **AI Coding Assistants (Gemini / GitHub Copilot)**: Used to assist in writing boilerplate code, debugging Docker configurations, and structuring skill execution logic.
- **LLM APIs (ChatGPT / Gemini)**: Used for brainstorming features, refining the system architecture, and drafting the user personas and documentation.

---

### 👥 Team ClawMentors
- **Sahana V S** — Team Lead & Core Development (RVCE CSE)

