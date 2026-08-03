"""
AI Coach component — Gemini-powered coaching advice with avatar.
"""

import streamlit as st
import pandas as pd
import urllib.parse

from utils.gemini import generate_text
from utils.prompts import get_coach_prompt, get_avatar_prompt
from utils.scoring import compute_productivity_score
from utils.ai_formatter import format_coach_response


def render_ai_coach(day_df: pd.DataFrame, coach_mode: str, selected_date: str):
    """Render the AI coaching section with advice, dynamic severity banner, and avatar."""

    st.subheader("🤖 AI Coach")

    if day_df.empty:
        st.warning("No data available for the selected date.")
        return

    total_minutes = int(day_df["Minutes_Used"].sum())
    productivity_score = compute_productivity_score(day_df)

    # Aggregating category breakdown using .to_string() (Phase 3, Step 8)
    category_summary = (
        day_df.groupby("Category")["Minutes_Used"]
        .sum()
        .reset_index()
        .to_string(index=False)
    )

    top_app_series = day_df.groupby("App_Name")["Minutes_Used"].sum()
    top_app = top_app_series.idxmax() if not top_app_series.empty else "N/A"

    # Status callout banner based on screen time severity (Phase 3, Step 10)
    if total_minutes > 360:
        st.error(
            f"🚨 **High Screen Time Warning!** You spent **{total_minutes} mins** ({total_minutes // 60}h {total_minutes % 60}m) on screen today. Action required!"
        )
    elif total_minutes > 240:
        st.warning(
            f"⚠️ **Moderate Screen Time Notice:** You logged **{total_minutes} mins** on screen today. Review your breakdown below."
        )
    else:
        st.info(
            f"✅ **Great Balance!** You stayed under control with **{total_minutes} mins** total screen time today."
        )

    col_coach, col_avatar = st.columns([2, 1])

    with col_coach:
        with st.spinner(f"Generating {coach_mode} coaching advice…"):
            prompt = get_coach_prompt(
                total_minutes=total_minutes,
                top_app=top_app,
                category_summary=category_summary,
                productivity_score=productivity_score,
                coach_mode=coach_mode,
                date=selected_date,
            )
            raw_advice = generate_text(prompt)
            advice = format_coach_response(raw_advice)

        st.markdown(advice)

    with col_avatar:
        avatar_prompt = get_avatar_prompt(total_minutes, productivity_score)
        encoded = urllib.parse.quote(avatar_prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}"

        st.image(
            image_url,
            caption=f"Your Digital Wellbeing Avatar — Score: {productivity_score}/100",
            use_container_width=True,
        )

