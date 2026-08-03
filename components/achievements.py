import streamlit as st
import pandas as pd

from utils.scoring import compute_productivity_score, weekly_streak


# =========================
# Achievement Definitions
# =========================

BADGES = [
    {
        "emoji": "🧘",
        "title": "Digital Detox",
        "desc": "Daily screen time below 2 hours",
        "check": lambda day_df, df, goal:
            day_df["Minutes_Used"].sum() < 120,
    },
    {
        "emoji": "🎯",
        "title": "Focus Master",
        "desc": "Productivity Score ≥ 80",
        "check": lambda day_df, df, goal:
            compute_productivity_score(day_df) >= 80,
    },
    {
        "emoji": "🔥",
        "title": "Consistent",
        "desc": "3-Day Streak Under Goal",
        "check": lambda day_df, df, goal:
            weekly_streak(df, goal) >= 3,
    },
    {
        "emoji": "🌅",
        "title": "Early Bird",
        "desc": "Coding / Education is Top Category",
        "check": lambda day_df, df, goal:
            (
                not day_df.empty and
                day_df.groupby("Category")["Minutes_Used"].sum().idxmax()
                in ["Coding", "Education"]
            ),
    },
    {
        "emoji": "⚔️",
        "title": "Screen Warrior",
        "desc": "5-Day Streak Under Goal",
        "check": lambda day_df, df, goal:
            weekly_streak(df, goal) >= 5,
    },
]


# =========================
# Render Cards
# =========================

def render_achievements(day_df: pd.DataFrame, df: pd.DataFrame, daily_goal: int):

    st.subheader("🏅 Achievements")

    earned = []
    locked = []

    for badge in BADGES:
        try:
            if badge["check"](day_df, df, daily_goal):
                earned.append(badge)
            else:
                locked.append(badge)
        except Exception:
            locked.append(badge)

    badges = earned + locked

    cols = st.columns(len(badges))

    for col, badge in zip(cols, badges):

        unlocked = badge in earned

        if unlocked:
            bg = "#DCFCE7"
            border = "#22C55E"
            status = "✅ Unlocked"
        else:
            bg = "#F3F4F6"
            border = "#9CA3AF"
            status = "🔒 Locked"

        with col:
            card_html = f"""<div style="background:{bg}; border:2px solid {border}; border-radius:14px; padding:14px 8px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); min-height:220px; display:flex; flex-direction:column; justify-content:space-between; align-items:center;">
<div style="font-size:42px; line-height:1.2; margin-bottom:6px;">{badge['emoji']}</div>
<div style="font-size:16px; font-weight:700; color:#111827; margin-bottom:6px; line-height:1.2;">{badge['title']}</div>
<div style="font-size:12px; color:#4B5563; line-height:1.3; margin-bottom:12px; min-height:36px;">{badge['desc']}</div>
<div style="background:white; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; color:#111827; border:1px solid {border}; display:inline-block;">{status}</div>
</div>"""
            st.markdown(card_html, unsafe_allow_html=True)