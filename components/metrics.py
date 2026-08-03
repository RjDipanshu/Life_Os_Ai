import streamlit as st


def show_metrics(day_df, daily_goal):

    total_minutes = day_df["Minutes_Used"].sum()

    top_app = (
        day_df.groupby("App_Name")["Minutes_Used"]
        .sum()
        .idxmax()
    )

    delta = total_minutes - daily_goal

    coding = day_df[
        day_df["Category"] == "Coding"
    ]["Minutes_Used"].sum()

    education = day_df[
        day_df["Category"] == "Education"
    ]["Minutes_Used"].sum()

    productivity_score = min(
        100,
        coding // 4 + education // 6
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🕒 Total Screen Time",
        f"{total_minutes} min"
    )

    c2.metric(
        "📱 Most Used App",
        top_app
    )

    c3.metric(
        "🎯 Goal Status",
        f"{delta:+} min",
        delta_color="inverse"
    )

    c4.metric(
        "⭐ Productivity",
        f"{productivity_score}/100"
    )
