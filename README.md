<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Powered-00BFFF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0wIDE4Yy00LjQxIDAtOC0zLjU5LTgtOHMzLjU5LTggOC04IDggMy41OSA4IDgtMy41OSA4LTggOHoiLz48L3N2Zz4=" alt="OpenClaw Powered"/>
  <img src="https://img.shields.io/badge/Samsung_PRISM-Hackathon_2026-1428A0?style=for-the-badge&logo=samsung&logoColor=white" alt="Samsung PRISM"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Groq-LLaMA_3.1-F55036?style=for-the-badge" alt="Groq"/>
  <img src="https://img.shields.io/badge/Telegram-Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>
</p>

<h1 align="center">🦞 ClawMentor Bharat</h1>

<h3 align="center">
  <em>An OpenClaw-Powered Autonomous Career Intelligence Agent<br/>for Indian Engineering Students</em>
</h3>

<p align="center">
  <strong>Samsung PRISM OpenClaw Hackathon 2026</strong><br/>
  Team: <strong>RVCE_ClawMentors</strong> · College: <strong>RV College of Engineering, Bengaluru</strong>
</p>

---

## 📑 Table of Contents

- [Project Video Demo](#-project-video-demo)
- [Project Presentation](#-project-presentation)
- [Problem Statement](#-problem-statement)
- [Our Solution](#-our-solution)
- [Key Features](#-key-features)
- [System Architecture](#%EF%B8%8F-system-architecture)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Deployment](#-setup--deployment)
- [Usage Guide](#-usage-guide)
- [AI Disclosure](#-ai-disclosure)
- [Team](#-team)

---

## 🎥 Project Video Demo

> **[▶️ Watch the Full Demo Video](https://drive.google.com/file/d/1_AZtuJ2z9fnawkDF0ECsTSgQKF33s5m2/view?usp=sharing)** — *Complete walkthrough of ClawMentor Bharat in action*

---

## 📊 Project Presentation

> **[📥 Download Presentation (PPTX)](./RVCE_ClawMentors.pptx)** — *Detailed slide deck explaining our architecture, features, and impact*

---

## 🎯 Problem Statement

Engineering students in India today face three critical challenges:

| Challenge | Impact |
|-----------|--------|
| **Information Overload** | Students are overwhelmed by scattered resources across platforms with no unified guidance |
| **Lack of Structured Career Guidance** | No personalized, data-driven mentorship tailored to individual skill levels and goals |
| **No Continuous Mentorship** | Traditional mentorship is sporadic — students need 24/7, proactive career intelligence |

These challenges result in students missing critical opportunities, developing skill gaps, and struggling to build competitive portfolios for top-tier placements.

---

## 💡 Our Solution

**ClawMentor Bharat** is a **24/7 Sovereign AI Career Sentinel** that acts as a student's personal career mentor. Built on the [OpenClaw](https://openclaw.ai) framework, it autonomously:

- 🧠 **Learns** the student's profile, goals, and current skill set
- 📊 **Analyzes** resume gaps and skill deficiencies in real-time
- 📋 **Plans** daily, personalized learning schedules
- 🔍 **Monitors** internship, research, and hackathon opportunities proactively
- 📈 **Tracks** weekly progress with professional reports
- 💬 **Communicates** via Telegram & WhatsApp for seamless interaction

> *From college desk to top-tier placement — ClawMentor Bharat guides every step.*

---

## ✨ Key Features

### 🧩 Core Skills

| # | Skill | Description |
|---|-------|-------------|
| 1 | **📋 Daily Learning Planner** | Generates realistic, time-blocked study plans tailored to the student's schedule and goals |
| 2 | **📄 Resume Gap Analyzer** | Uses PyMuPDF to parse resumes, detect missing technical skills, and suggest immediate improvements |
| 3 | **🚀 Project Recommendation Engine** | Suggests high-impact portfolio projects that specifically target detected skill gaps |
| 4 | **🔍 Opportunity Tracker** | Proactively monitors ArXiv, GitHub, and hackathon platforms for internship and research alerts |
| 5 | **📊 Weekly Progress Digest** | Aggregates weekly performance into professional Microsoft Word (`.docx`) summary reports |
| 6 | **🔧 Repository Analyzer & Build Engine** | Analyzes GitHub repos for tech stack detection and build feasibility assessment |
| 7 | **📝 Meeting Scribe & Prep Coach** | Transcribes meetings and auto-generates structured action items |

### 🔔 Proactive Multi-Channel Notifications
Real-time alerts via **Telegram** and **WhatsApp (Twilio)** for all career events — new opportunities, daily plans, weekly digests, and skill gap alerts are delivered directly to the student.

### 🧠 Persistent Cognitive Memory
Utilizes OpenClaw's Durable Memory system for cross-session continuity:

| Memory File | Purpose |
|-------------|---------|
| `SOUL.md` | Agent persona, behavioral logic, and core identity |
| `USER.md` | Student profile, career goals, and preferences |
| `ROADMAP.md` | Living progress tracker with milestones and skill gaps |
| `HEARTBEAT.md` | Autonomous task scheduler for proactive actions |

---

## 🏗️ System Architecture

ClawMentor Bharat is built on the **OpenClaw 5-Layer Stack**:

```
┌─────────────────────────────────────────────────────────┐
│                   📱 Communication Layer                │
│              Telegram Bot  ·  WhatsApp (Twilio)         │
├─────────────────────────────────────────────────────────┤
│                   🔄 Channel Adapter                    │
│       Normalizes cross-platform messaging → Intents     │
├─────────────────────────────────────────────────────────┤
│                   🚪 Gateway Layer                      │
│        Session Mgmt · Memory Routing · Auth             │
├─────────────────────────────────────────────────────────┤
│                   🧠 Pi Engine (Core AI)                │
│     Groq LLaMA 3.1 · Roadmap Updates · Gap Detection   │
├─────────────────────────────────────────────────────────┤
│                   ⚙️ Skill Execution Layer              │
│    7 Sandboxed Python Modules (see Key Features)        │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Core Framework** | [OpenClaw](https://openclaw.ai) — Sovereign AI Agent Platform |
| **Language Intelligence** | Groq Cloud — LLaMA 3.1 8B Instant |
| **Skill Modules** | Python 3.x |
| **Gateway Runtime** | TypeScript (Node.js) |
| **Communication** | Telegram Bot API · Twilio WhatsApp API |
| **Libraries** | PyMuPDF · python-docx · twilio · python-dotenv |
| **Infrastructure** | Docker Compose · OpenClaw Tank |
| **Memory System** | Markdown-based Durable Cognitive Memory |

---

## 📁 Project Structure

```
ClawMentor-Bharat/
├── memory/                         # 🧠 Durable Cognitive Memory
│   ├── SOUL.md                     #    Agent persona & behavioral logic
│   ├── USER.md                     #    Student profile & career goals
│   ├── ROADMAP.md                  #    Living progress tracker
│   └── HEARTBEAT.md                #    Autonomous task scheduler
│
├── skills/                         # ⚙️ Specialized Skill Modules
│   ├── daily_learning_planner/     #    Personalized study plans
│   ├── resume_gap_analyzer/        #    Resume parsing & gap detection
│   ├── project_recommendation/     #    Portfolio project suggestions
│   ├── opportunity_tracker/        #    Internship & research alerts
│   ├── weekly_progress_digest/     #    .docx weekly summaries
│   ├── repo_analyzer/              #    GitHub repo analysis
│   └── meeting_scribe/             #    Meeting transcription
│
├── scripts/                        # 🔧 Utility scripts
├── utils/                          # 🛠️ Helper modules
│
├── docker-compose.yml              # 🐳 Sovereign deployment config
├── openclaw.json                   # ⚙️ Agent & model configuration
├── requirements.txt                # 📦 Python dependencies
│
├── SOUL.md                         # 🪪 Root persona definition
├── USER.md                         # 👤 Root user profile
├── IDENTITY.md                     # 🆔 Agent identity
├── SKILL.md                        # 📋 Skill manifest
├── ROADMAP.md                      # 🗺️ Root roadmap
├── HEARTBEAT.md                    # 💓 Root scheduler
│
├── RVCE_ClawMentors.pptx           # 📊 Hackathon presentation
├── OpenClaw_AI_Disclosure.pdf      # 🤖 AI disclosure document
└── README.md                       # 📖 This file
```

---

## 🚀 Setup & Deployment

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) & Docker Compose installed
- [OpenClaw CLI](https://openclaw.ai) installed
- Groq API key ([get one free](https://console.groq.com))
- Telegram Bot Token ([create via @BotFather](https://t.me/BotFather))

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/sahanavs-2006/ClawMentor-Bharat.git
cd ClawMentor-Bharat

# 2. Configure environment variables
cp .env.example .env
# Edit .env with your API keys:
#   GROQ_API_KEY=your_groq_key
#   TELEGRAM_BOT_TOKEN=your_bot_token
#   OPENCLAW_GATEWAY_TOKEN=your_gateway_token

# 3. Install Python dependencies (for skill modules)
pip install -r requirements.txt

# 4. Deploy ClawMentor Bharat
docker-compose up -d

# 5. Verify deployment
docker logs clawmentor-bharat
# Look for: "[gateway] ready" and "[telegram] starting provider"
```

### Verify Everything is Running

```bash
# Check container health
docker ps -f name=clawmentor-bharat

# View live logs
docker logs -f clawmentor-bharat

# Access the dashboard
# Open: http://localhost:18789
```

---

## 🎮 Usage Guide

Once deployed, ClawMentor Bharat runs as an **autonomous background agent**:

| Action | How |
|--------|-----|
| **💬 Chat with the Agent** | Send messages via **Telegram** (`@clawmentor_bharat_bot`) or the **OpenClaw Dashboard** (`http://localhost:18789`) |
| **👤 Profile Setup** | The agent reads `memory/USER.md` to understand goals and initializes a `HEARTBEAT.md` scheduler |
| **📈 Track Progress** | Check `memory/ROADMAP.md` — the agent continuously updates your career roadmap and milestones |
| **🔔 Receive Alerts** | Get proactive daily plans, opportunity alerts, and weekly `.docx` summaries automatically |
| **🧠 Persistent Context** | The agent remembers everything across sessions via its durable memory system |

---

## 🤖 AI Disclosure

> **[📄 View Full AI Disclosure (PDF)](./OpenClaw_AI_Disclosure.pdf)**

This project was developed with the assistance of the following AI tools:

| AI Tool | Usage |
|---------|-------|
| **Groq / LLaMA 3.1** | Powers the core reasoning engine, gap detection, and learning plan generation |
| **AI Coding Assistants** (Gemini / Copilot) | Assisted with boilerplate code, Docker debugging, and skill module structuring |
| **LLM APIs** (ChatGPT / Gemini) | Used for feature brainstorming, architecture refinement, and documentation drafting |

---

## 👥 Team

<table>
  <tr>
    <td align="center">
      <strong>Sahana V S</strong><br/>
      Team Lead & Core Development<br/>
      <em>RV College of Engineering — CSE</em><br/>
      <a href="https://github.com/sahanavs-2006">GitHub</a>
    </td>
  </tr>
</table>

---

<p align="center">
  <strong>🦞 ClawMentor Bharat — Your Sovereign AI Career Sentinel</strong><br/>
  <em>Built for Samsung PRISM OpenClaw Hackathon 2026</em><br/><br/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square" alt="Status"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"/>
</p>
