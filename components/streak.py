"""
Streak component — consecutive goal-met days indicator.
"""

import streamlit as st
from utils.scoring import weekly_streak
import pandas as pd


def render_streak(df: pd.DataFrame, daily_goal: int):
    """Render the current streak badge in the sidebar."""

    streak = weekly_streak(df, daily_goal)

    if streak == 0:
        emoji = "😔"
        label = "No streak yet"
        colour = "#ff6b6b"
    elif streak < 3:
        emoji = "🔥"
        label = f"{streak}-day streak!"
        colour = "#ffa726"
    else:
        emoji = "🏆"
        label = f"{streak}-day streak!"
        colour = "#66bb6a"

    st.sidebar.markdown(
        f"""<div style="background:{colour}22; border:1px solid {colour}; border-radius:8px; padding:10px 14px; text-align:center; margin-bottom:8px;">
<span style="font-size:1.6rem;">{emoji}</span><br>
<strong style="color:{colour};">{label}</strong><br>
<small style="color:gray;">Days under goal</small>
</div>""",
        unsafe_allow_html=True,
    )
