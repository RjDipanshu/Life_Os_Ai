"""
Header component — branded title strip with live date/time.
"""

import streamlit as st
from datetime import datetime


def render_header():
    """Render the Life-OS AI branded header."""

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            "<h1 style='margin-bottom:0'>🧠 Life-OS AI</h1>"
            "<p style='margin-top:4px; color:gray; font-size:1rem;'>"
            "Your AI-Powered Digital Wellbeing Dashboard"
            "</p>",
            unsafe_allow_html=True,
        )

    with col2:
        now = datetime.now()
        date_str = now.strftime("%A, %d %b %Y")
        time_str = now.strftime("%I:%M %p")
        st.markdown(
            f"<div style='text-align:right; padding-top:8px;'>"
            f"<span style='font-size:0.85rem; color:gray;'>"
            f"{date_str}<br>{time_str}"
            f"</span>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.divider()
