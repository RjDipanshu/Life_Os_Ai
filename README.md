# 🧠 Life-OS AI — Digital Wellbeing Dashboard

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ██╗     ██╗███████╗███████╗   ██████╗ ███████╗     █████╗ ██╗             │
│   ██║     ██║██╔════╝██╔════╝  ██╔═══██╗██╔════╝    ██╔══██╗██║             │
│   ██║     ██║█████╗  █████╗    ██║   ██║███████╗    ███████║██║             │
│   ██║     ██║██╔══╝  ██╔══╝    ██║   ██║╚════██║    ██╔══██║██║             │
│   ███████╗██║██║     ███████╗  ╚██████╔╝███████║    ██║  ██║██║             │
│   ╚══════╝╚═╝╚═╝     ╚══════╝   ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝             │
│                                                                             │
│            AI-POWERED PRODUCTIVITY & LIFESTYLE WELLBEING OS                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

> **Track:** AI Builder  
> **Capstone:** "Life-OS" Wellbeing Dashboard  
> **Tech Stack:** Python 3.11 | Streamlit | Pandas | Gemini AI (google-genai) | Pollinations AI


<img width="1917" height="868" alt="image" src="https://github.com/user-attachments/assets/ac9238ad-da37-46cf-b949-ed1eeb2ee263" />


<img width="1917" height="867" alt="image" src="https://github.com/user-attachments/assets/2c9a1811-d295-4afe-a44a-2544237ba4ec" />


<img width="1907" height="862" alt="image" src="https://github.com/user-attachments/assets/6edc7ac3-337a-483e-9132-89649a66e32c" />


<img width="1917" height="866" alt="image" src="https://github.com/user-attachments/assets/c3e15295-3227-465c-b774-1723a21d06c1" />

---

## ⚡ System Diagnostics

```bash
$ life-os status --all

[SYS_INFO] OS Protocol      : Active
[DATA_PIPE] Source CSV      : data/screentime.csv (14 Days Logged)
[AI_ENGINE] Model           : gemini-2.0-flash
[INTERFACE] Streamlit UI    : SaaS Dashboard (Wide Layout)
[DELIVERABLE] Hidden Gems   : Shareable Accountability Link + Guilt-Trip Avatar
[STATUS] Deploy Ready       : YES (100% Compliant)
```

---

## 🚀 Key Features

* 📊 **Data Pipeline:** 14+ days of structured screen-time tracking across 7+ app categories.
* 🎯 **Command Center UI:** Sidebar date filter, custom daily goal sliders, Pomodoro focus timer, & streak badge.
* 📈 **KPI Row:** `st.metric` cards with inverse delta coloring showing screen time vs daily goal.
* 📉 **Interactive Charts:** Daily trends, category bar charts, usage heatmaps, and weekly analytics.
* 🤖 **Gemini AI Coach:** Direct data bridge converting pandas aggregations (`.to_string()`) into personalized physical lifestyle swap recommendations.
* 👹 **Guilt-Trip Avatar:** Dynamic AI visual avatar generated via Pollinations API reflecting daily productivity score.
* 🔗 **Shareable Accountability Link:** URL query parameter integration (`st.query_params`) to broadcast stats instantly.
* 📄 **Weekly AI Wellness Report:** Automated downloadable PDF/TXT executive summary powered by Gemini.

---

## 📂 Project Architecture

```text
Life-OS-AI/
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Verified Python dependencies
├── README.md               # Terminal-style project documentation
├── .env                    # Hidden local environment variables (GEMINI_API_KEY)
├── .gitignore              # Configured git exclusion rules
├── data/
│   └── screentime.csv      # 14-day synthetic digital wellbeing dataset
├── components/             # Modular Streamlit UI components
│   ├── achievements.py     # Unlocked badge grid
│   ├── ai_coach.py         # AI coaching & dynamic avatar rendering
│   ├── analytics.py        # Advanced analytical breakdowns
│   ├── charts.py           # Trend line, bar, pie & heatmap visualisations
│   ├── header.py           # Dashboard header strip with timestamp
│   ├── metrics.py          # KPI metrics row with goal deltas
│   ├── progress.py         # Progress bars and usage status
│   ├── quote.py            # Daily motivational quote block
│   ├── sidebar.py          # Interactive controls & pomodoro timer
│   ├── streak.py           # Consecutive goal meeting badge
│   └── weekly_report.py    # Weekly AI summary report & export
├── utils/                  # Backend utilities & AI prompt engines
│   ├── ai_formatter.py     # AI markdown response formatter
│   ├── gemini.py           # Google GenAI SDK client wrapper
│   ├── prompts.py          # System prompts for life coaching & avatars
│   └── scoring.py          # Productivity score & streak algorithms
└── styles/
    └── style.css           # Custom CSS styling system
```

---

## ⚙️ Quick Start

```bash
# 1. Clone Repository
$ git clone https://github.com/your-username/Life-OS-AI.git
$ cd Life-OS-AI

# 2. Virtual Environment Setup
$ python -m venv venv
$ source venv/bin/activate       # macOS / Linux
$ venv\Scripts\activate          # Windows

# 3. Dependencies Installation
$ pip install -r requirements.txt

# 4. Environment Key Configuration
$ echo "GEMINI_API_KEY=your_gemini_api_key" > .env

# 5. Launch Dashboard
$ streamlit run app.py
```

---

## 📋 Capstone Requirements Audit

| Assignment Phase | Feature | Status | Implementation Details |
| :--- | :--- | :---: | :--- |
| **Phase 1** | 14-Day Dataset | ✅ | `data/screentime.csv` (Date, App_Name, Category, Minutes_Used) |
| **Phase 1** | Data Ingestion | ✅ | `pd.read_csv("data/screentime.csv")` in `app.py` |
| **Phase 2** | Sidebar Controls | ✅ | `st.sidebar.selectbox` & `st.slider` for Daily Goal |
| **Phase 2** | KPI Row | ✅ | `st.metric` with `delta_color="inverse"` in `components/metrics.py` |
| **Phase 2** | Visualizations | ✅ | Trend line, category bar chart, pie, heatmap in `components/charts.py` |
| **Phase 3** | Data Bridge | ✅ | Aggregates daily category minutes with `.to_string()` |
| **Phase 3** | Gemini System Prompt| ✅ | f-string prompt requiring physical activity replacements |
| **Phase 3** | Dynamic Severity Banner| ✅ | `st.info` / `st.warning` / `st.error` based on usage severity |
| **Phase 4** | Hidden Gem #1 | ✅ | **Guilt-Trip Avatar:** Dynamic Pollinations AI prompt |
| **Phase 4** | Hidden Gem #2 | ✅ | **Accountability Link:** `st.query_params["screen"]` |

---

