import streamlit as st


def weekly_analytics(df):

    total = (
        df.groupby("Date")["Minutes_Used"]
        .sum()
    )

    best_day = total.idxmin()
    worst_day = total.idxmax()

    average = round(total.mean(), 1)

    st.subheader("📈 Weekly Analytics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🏆 Best Day",
        best_day
    )

    c2.metric(
        "⚠ Worst Day",
        worst_day
    )

    c3.metric(
        "📊 Daily Average",
        f"{average} min"
    )
