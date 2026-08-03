"""
Prompt templates for Gemini AI interactions.
"""


def get_coach_prompt(
    total_minutes: int,
    top_app: str,
    category_summary: str,
    productivity_score: int,
    coach_mode: str,
    date: str
) -> str:
    """Generate a personalised coaching prompt based on usage data."""

    tone_map = {
        "Friendly 😊": "You are a warm, supportive friend who gently encourages better habits.",
        "Strict 😐": "You are a no-nonsense productivity coach who gives direct, brutal-but-fair feedback.",
        "Motivational 🔥": "You are an energetic hype coach who fires people up with passion.",
        "Military 💂": "You are a drill sergeant giving crisp, commanding orders.",
        "Therapist 🧠": "You are a mindful therapist who helps users reflect on their digital habits.",
    }

    tone = tone_map.get(coach_mode, tone_map["Friendly 😊"])

    return f"""
{tone}

You are acting as a holistic life coach analyzing digital screen time data.

Screen time summary for {date}:
- Total Screen Time: {total_minutes} minutes
- Most Used App: {top_app}
- Productivity Score: {productivity_score}/100

Category Breakdown (Category -> Minutes):
{category_summary}

REQUIREMENT:
Do NOT just say "use your phone less". You MUST analyze the screen time categories above (especially Social Media / Entertainment) and suggest specific physical, real-world activity replacements (e.g. 45 min workout, outdoor walk, meal prepping, reading a book).

Provide:
1. Direct Habit Assessment (2 sentences analyzing their balance)
2. 3 Specific Real-World Activity Replacements for high-screen categories
3. A punchy closing motivational line

Keep the total response under 200 words and strictly maintain the {coach_mode} persona.
""".strip()


def get_avatar_prompt(total_minutes: int, productivity_score: int) -> str:
    """Generate an avatar image prompt based on screen time and productivity."""

    if productivity_score >= 70:
        return "Focused student working diligently on a laptop in a bright, organized study space, determined expression, warm lighting"
    elif productivity_score >= 40:
        return "Young professional at a desk, half-focused on work, coffee in hand, slightly tired but still engaged"
    else:
        return "Tired zombie slumped on a couch, scrolling endlessly on a phone, surrounded by junk food, dark room"


def get_weekly_report_prompt(
    avg_minutes: float,
    best_day: str,
    worst_day: str,
    top_category: str,
    total_weekly: int
) -> str:
    """Generate a weekly AI report prompt."""

    return f"""
You are a data-driven productivity analyst.

Weekly screen time summary:
- Total screen time this week: {total_weekly} minutes
- Daily average: {avg_minutes} minutes
- Best (lowest usage) day: {best_day}
- Worst (highest usage) day: {worst_day}
- Most used category: {top_category}

Write a professional weekly wellness report that includes:
1. A performance summary paragraph
2. Key insights (what the data reveals)
3. Three concrete goals for next week
4. Overall digital health rating (Excellent / Good / Fair / Poor)

Keep it under 300 words, use a professional but friendly tone.
""".strip()
