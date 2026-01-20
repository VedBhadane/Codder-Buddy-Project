# Coder Buddy: Autonomous AI Software Engineer 🤖

**Coder Buddy** is an advanced multi-agent AI system designed to automate the software development lifecycle. Unlike standard coding assistants that merely provide snippets, Coder Buddy acts as a **full engineering team**—planning, architecting, and writing code to generate deployable multi-file projects from a single prompt.

Turn natural language ideas into fully functional web applications (HTML, CSS, JavaScript) in seconds.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![AI](https://img.shields.io/badge/LLM-Llama_3.3_70B-purple)
![Orchestration](https://img.shields.io/badge/Orchestration-LangGraph-orange)

## 🌟 Key Features

* **Zero-Shot Project Generation:** Generates complete, multi-file applications (e.g., "Snake Game", "Todo List") from a single sentence.
* **Multi-Agent Architecture:** Utilizes a specialized triad of agents (**Planner**, **Architect**, **Coder**) to ensure logical consistency and structural integrity.
* **Stateful Orchestration:** Built on **LangGraph**, allowing agents to share memory, maintain context across files, and self-correct during execution.
* **Automated File I/O:** Directly writes, organizes, and manages files in your local file system—no copy-pasting required.
* **High-Velocity Inference:** Optimized for speed using **Groq** (Llama 3.3 70B) for near-instant planning and coding.

---

## 🧠 The Architecture (The "Brain")

Coder Buddy replaces linear "chain-of-thought" generation with a **Stateful Directed Acyclic Graph (DAG)**.

| Agent | Role | Responsibility |
| :--- | :--- | :--- |
| **Planner** | Product Manager | Analyzes the user prompt, determines the tech stack, and lists core features. |
| **Architect** | Solutions Architect | Creates a file structure blueprint and defines technical dependencies (e.g., matching CSS classes to HTML IDs). |
| **Coder** | Developer | Executes the blueprint loop, writing valid code to disk and ensuring all files are linked correctly. |

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Orchestration:** LangGraph
* **LLM Inference:** Groq API (Llama-3.3-70b-versatile)
* **Validation:** Pydantic (Structured Data Extraction)
* **Package Manager:** UV (High-performance Python package installer)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/coder-buddy.git](https://github.com/yourusername/coder-buddy.git)
cd coder-buddy

```

### 2. Install Dependencies

We use **uv** for extremely fast dependency management.

```bash
# Install uv (if not already installed)
pip install uv

# Create virtual environment and install packages
uv venv
uv pip install -r requirements.txt

```

### 3. Configure API Keys

Create a `.env` file in the root directory and add your Groq API key:

```ini
GROQ_API_KEY=gsk_your_groq_api_key_here

# Optional: For LangSmith tracing
# LANGCHAIN_API_KEY=... 
# LANGCHAIN_TRACING_V2=true

```

---

## 🚀 Usage

Run the main application script:

```bash
uv run python main.py

```

### Example Workflow

**Terminal Prompt:** `Enter your project prompt:`
**User Input:**

> "Build a dark-mode Pomodoro timer with a neon aesthetic and sound alerts."

**Process:**

1. **Planner** creates the feature list...
2. **Architect** maps `index.html`, `style.css`, `script.js`...
3. **Coder** writes the actual code to `/generated_project`...

**Result:** Go to the `generated_project/` folder and open `index.html` in your browser to see your app!

---

## 📂 Project Structure

```text
coder-buddy/
├── agent/
│   ├── graph.py       # Main LangGraph definition (Nodes & Edges)
│   ├── agents.py      # Logic for Planner, Architect, and Coder
│   ├── prompts.py     # System instructions (Prompt Engineering)
│   ├── states.py      # Pydantic models for State management
│   └── tools.py       # File system tools (write_file, read_file)
├── generated_project/ # Output directory for AI-created apps
├── main.py            # Entry point (CLI)
├── requirements.txt   # Python dependencies
└── .env               # API Keys

```

---

## 🗺️ Future Roadmap

* [ ] **Self-Correction Loop:** Add a "Tester Agent" to run the code and fix syntax errors automatically.
* [ ] **Vision-to-Code:** Allow users to upload whiteboard sketches as input prompts using Gemini Pro Vision.
* [ ] **Streamlit UI:** Replace the CLI with a web-based chat interface.
* [ ] **One-Click Deployment:** Integrate Vercel/Netlify API to publish apps instantly.

---

**Author:** Vedant Manohar Bhadane

