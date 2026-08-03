"""
Sidebar component — control panel, Pomodoro timer, weekly goal, about.
"""

import streamlit as st
import pandas as pd
from components.streak import render_streak


def sidebar(df: pd.DataFrame):
    """Render the full sidebar and return user-selected settings."""

    st.sidebar.title("⚙️ Control Panel")

    # ── Date & Goal ───────────────────────────────────────────────────────────
    selected_date = st.sidebar.selectbox(
        "📅 Select Date",
        sorted(df["Date"].unique(), reverse=True),
    )

    daily_goal = st.sidebar.slider(
        "🎯 Daily Goal (Minutes)",
        min_value=60,
        max_value=600,
        value=240,
        step=30,
    )

    # ── Weekly Goal ───────────────────────────────────────────────────────────
    weekly_goal = st.sidebar.number_input(
        "📆 Weekly Screen-Time Goal (min)",
        min_value=300,
        max_value=5000,
        value=1500,
        step=100,
    )

    # ── Coach Personality ─────────────────────────────────────────────────────
    coach_mode = st.sidebar.selectbox(
        "🤖 Coach Personality",
        [
            "Friendly 😊",
            "Strict 😐",
            "Motivational 🔥",
            "Military 💂",
            "Therapist 🧠",
        ],
    )

    # ── Theme ─────────────────────────────────────────────────────────────────
    theme = st.sidebar.selectbox(
        "🎨 Theme",
        ["Light", "Dark"],
    )

    st.sidebar.divider()

    # ── Streak Badge ──────────────────────────────────────────────────────────
    render_streak(df, daily_goal)

    st.sidebar.divider()

    # ── Pomodoro Timer ────────────────────────────────────────────────────────
    st.sidebar.subheader("⏱️ Pomodoro Timer")

    focus_time = st.sidebar.slider(
        "Focus Time (minutes)",
        min_value=15,
        max_value=60,
        value=25,
        step=5,
        key="pomodoro_slider",
    )

    if st.sidebar.button("▶ Start Focus Session", key="start_pomodoro"):
        st.sidebar.success(
            f"🍅 Pomodoro started for **{focus_time} minutes**.\n\n"
            "Stay focused — no social media!"
        )

    st.sidebar.divider()

    # ── Weekly Progress ───────────────────────────────────────────────────────
    weekly_total = int(
        df.groupby("Date")["Minutes_Used"].sum().sum()
    )
    weekly_pct = min(1.0, weekly_total / weekly_goal)

    st.sidebar.subheader("📆 Weekly Progress")
    st.sidebar.progress(
        weekly_pct,
        text=f"{weekly_total} / {weekly_goal} min ({weekly_pct*100:.0f}%)",
    )

    st.sidebar.divider()

    # ── Leaderboard Card ──────────────────────────────────────────────────────
    daily_totals = df.groupby("Date")["Minutes_Used"].sum()
    best_day_total = int(daily_totals.min())
    best_day_label = "Lowest Usage Day"

    if best_day_total < 240:
        rank_delta = "Healthy Week 🌿"
    elif best_day_total < 360:
        rank_delta = "Average Week 😐"
    else:
        rank_delta = "Heavy Usage Week ⚠️"

    st.sidebar.metric(
        label="🏆 Leaderboard Rank",
        value="#1",
        delta=rank_delta,
    )

    st.sidebar.divider()

    # ── About ─────────────────────────────────────────────────────────────────
    with st.sidebar.expander("ℹ️ About Life-OS AI"):
        st.write(
            """
            **Life-OS AI** helps you understand your screen habits
            and receive AI-powered productivity coaching.

            Built with **Streamlit** + **Gemini AI** 🤖

            - 📊 Real-time analytics
            - 🤖 Personalised AI coaching
            - 🏅 Achievement badges
            - ⏱️ Pomodoro timer
            - 📄 Weekly AI reports
            """
        )

    st.sidebar.info(
        "💡 Reduce unnecessary screen time and build healthier digital habits."
    )

    return selected_date, daily_goal, coach_mode, theme
