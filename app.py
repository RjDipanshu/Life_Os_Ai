"""
Life-OS AI — Main Application Entry Point
"""

import streamlit as st
import pandas as pd

# ── Utils ─────────────────────────────────────────────────────────────────────
from utils.scoring import calculate_scores

# ── Components ────────────────────────────────────────────────────────────────
from components.sidebar import sidebar
from components.header import render_header
from components.metrics import show_metrics
from components.charts import (
    daily_trend_chart,
    category_bar_chart,
    category_pie,
    usage_heatmap,
    top_apps_chart,
    weekly_trend_chart,
    category_ranking_table,
)
from components.analytics import weekly_analytics
from components.progress import render_progress
from components.quote import render_quote
from components.ai_coach import render_ai_coach
from components.achievements import render_achievements
from components.weekly_report import render_weekly_report

# ── Page Config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Life-OS AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load CSS ──────────────────────────────────────────────────────────────────

def load_css():
    try:
        with open("styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )
    except FileNotFoundError:
        pass

load_css()

# ── Load Dataset ──────────────────────────────────────────────────────────────

df = pd.read_csv("data/screentime.csv")

# ── Sidebar ───────────────────────────────────────────────────────────────────

selected_date, daily_goal, coach_mode, theme = sidebar(df)

# ── Filter to selected day ────────────────────────────────────────────────────

day_df = df[df["Date"] == selected_date]

# ── Compute Scores ────────────────────────────────────────────────────────────

scores = calculate_scores(day_df, daily_goal)

# ── Header ────────────────────────────────────────────────────────────────────

render_header()

# ── Motivational Quote ────────────────────────────────────────────────────────

render_quote()

st.divider()

# ── Metrics ───────────────────────────────────────────────────────────────────

show_metrics(day_df, daily_goal)

st.divider()

# ── Goal Progress + Screen-Time Status ───────────────────────────────────────

render_progress(day_df, daily_goal)

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────

col1, col2 = st.columns(2)

with col1:
    daily_trend_chart(df)

with col2:
    category_bar_chart(day_df)

st.divider()

category_pie(day_df)

st.divider()

# ── Advanced Visualisations (Milestone 8) ────────────────────────────────────

st.subheader("🔥 Advanced Visualisations")

col3, col4 = st.columns(2)

with col3:
    usage_heatmap(df)

with col4:
    weekly_trend_chart(df)

st.divider()

# ── Top Apps + Category Ranking ───────────────────────────────────────────────

col5, col6 = st.columns(2)

with col5:
    st.subheader("📱 Top Apps")
    top_apps_chart(df)

with col6:
    st.subheader("🏆 Category Ranking")
    category_ranking_table(df)

st.divider()

# ── Weekly Analytics ──────────────────────────────────────────────────────────

weekly_analytics(df)

st.divider()

# ── Achievements ──────────────────────────────────────────────────────────────

render_achievements(day_df, df, daily_goal)

st.divider()

# ── AI Coach + Avatar ─────────────────────────────────────────────────────────

st.header("🤖 AI Productivity Coach")
st.write(
    "Get personalised lifestyle and productivity advice "
    "based on today's screen usage."
)

render_ai_coach(day_df, coach_mode, selected_date)

st.divider()

# ── AI Weekly Report + Export ─────────────────────────────────────────────────

render_weekly_report(df)

st.divider()

# ── Data Preview + Download CSV (Step 6) ──────────────────────────────────────

st.subheader("📂 Today's Data")

st.dataframe(day_df, use_container_width=True)

st.download_button(
    label="⬇️ Download Today's Data",
    data=day_df.to_csv(index=False),
    file_name="today.csv",
    mime="text/csv",
    key="download_today",
)

# ── Accountability Link (Step 7) ──────────────────────────────────────────────

total_today = scores["total"]

st.subheader("🔗 Accountability Link")
st.info(
    f"Share your screen time with a friend! "
    f"Append `?screen={total_today}` to this app's URL."
)
st.query_params["screen"] = str(total_today)

st.code(f"?screen={total_today}", language=None)

st.divider()

# ── Footer ───────────────────────────────────────────────────────────────────