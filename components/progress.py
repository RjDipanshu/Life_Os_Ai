import streamlit as st


def render_progress(day_df, daily_goal):
    """
    Display goal progress and wellness status.
    """

    total_minutes = int(day_df["Minutes_Used"].sum())

    progress = min(total_minutes / daily_goal, 1.0)

    st.subheader("🎯 Daily Goal Progress")

    st.progress(progress)

    st.write(f"**Today's Usage:** {total_minutes} min")
    st.write(f"**Daily Goal:** {daily_goal} min")

    if total_minutes <= daily_goal:
        st.success("✅ Great! You stayed within your daily goal.")
    else:
        st.warning(
            f"⚠️ You exceeded your goal by {total_minutes - daily_goal} minutes."
        )