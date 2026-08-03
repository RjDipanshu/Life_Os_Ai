"""
Weekly Report component — AI-generated report with download button.
"""

import streamlit as st
import pandas as pd
from datetime import datetime

from utils.gemini import generate_text
from utils.prompts import get_weekly_report_prompt
from utils.ai_formatter import format_report


def render_weekly_report(df: pd.DataFrame):
    """Render the AI-generated weekly wellness report with export."""

    st.subheader("📋 AI Weekly Wellness Report")

    daily_totals = df.groupby("Date")["Minutes_Used"].sum()
    avg_minutes = round(daily_totals.mean(), 1)
    best_day = daily_totals.idxmin()
    worst_day = daily_totals.idxmax()
    total_weekly = int(daily_totals.sum())

    top_category_series = df.groupby("Category")["Minutes_Used"].sum()
    top_category = top_category_series.idxmax() if not top_category_series.empty else "N/A"

    col1, col2, col3 = st.columns(3)
    col1.metric("📅 Best Day", best_day)
    col2.metric("⚠️ Worst Day", worst_day)
    col3.metric("📊 Weekly Total", f"{total_weekly} min")

    with st.expander("🤖 Generate AI Report", expanded=False):
        if st.button("✨ Generate Weekly Report", key="gen_weekly_report"):
            with st.spinner("Analysing your week with Gemini AI…"):
                prompt = get_weekly_report_prompt(
                    avg_minutes=avg_minutes,
                    best_day=best_day,
                    worst_day=worst_day,
                    top_category=top_category,
                    total_weekly=total_weekly,
                )
                raw_report = generate_text(prompt)
                today = datetime.now().strftime("%Y-%m-%d")
                formatted = format_report(raw_report, today)

            st.markdown(formatted)

            st.download_button(
                label="📄 Download AI Report",
                data=formatted,
                file_name="LifeOS_Report.txt",
                mime="text/plain",
                key="download_report",
            )
