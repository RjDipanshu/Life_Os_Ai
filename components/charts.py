"""
Charts component — all Plotly visualisations for Life-OS AI.
"""

import streamlit as st
import plotly.express as px
import pandas as pd


# ── Existing Charts ──────────────────────────────────────────────────────────

def daily_trend_chart(df: pd.DataFrame):
    """Line chart of daily total screen time."""

    trend = (
        df.groupby("Date")["Minutes_Used"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="Date",
        y="Minutes_Used",
        markers=True,
        title="📈 Daily Screen Time Trend",
        color_discrete_sequence=["#667eea"],
    )

    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)


def category_bar_chart(day_df: pd.DataFrame):
    """Bar chart of category usage for the selected day."""

    category = (
        day_df.groupby("Category")["Minutes_Used"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Minutes_Used",
        color="Category",
        title="📊 Category Usage",
    )

    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)


def category_pie(day_df: pd.DataFrame):
    """Pie / donut chart of screen time distribution."""

    category = (
        day_df.groupby("Category")["Minutes_Used"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        values="Minutes_Used",
        names="Category",
        title="🥧 Screen Time Distribution",
        hole=0.4,
    )

    st.plotly_chart(fig, use_container_width=True)


# ── Milestone 8 Charts ───────────────────────────────────────────────────────

def usage_heatmap(df: pd.DataFrame):
    """Density heatmap of screen time over dates."""

    daily = (
        df.groupby("Date")["Minutes_Used"]
        .sum()
        .reset_index()
    )

    fig = px.density_heatmap(
        daily,
        x="Date",
        y="Minutes_Used",
        title="🌡️ Screen Time Heatmap",
        color_continuous_scale="Viridis",
        nbinsy=20,
    )

    fig.update_layout(height=380)
    st.plotly_chart(fig, use_container_width=True)


def top_apps_chart(df: pd.DataFrame):
    """Horizontal bar chart of top apps by total usage."""

    top = (
        df.groupby("App_Name")["Minutes_Used"]
        .sum()
        .sort_values(ascending=True)
        .tail(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="Minutes_Used",
        y="App_Name",
        orientation="h",
        title="📱 Top 10 Apps by Usage",
        color="Minutes_Used",
        color_continuous_scale="Blues",
    )

    fig.update_layout(height=420, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def weekly_trend_chart(df: pd.DataFrame):
    """Area chart of weekly screen time trend."""

    weekly = (
        df.groupby("Date")["Minutes_Used"]
        .sum()
        .reset_index()
    )

    fig = px.area(
        weekly,
        x="Date",
        y="Minutes_Used",
        title="📅 Weekly Screen Time Overview",
        color_discrete_sequence=["#764ba2"],
    )

    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)


def category_ranking_table(df: pd.DataFrame):
    """Display category ranking as a styled dataframe."""

    rank = (
        df.groupby("Category")["Minutes_Used"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"Minutes_Used": "Total Minutes"})
    )

    rank.index = rank.index + 1  # 1-based ranking
    rank.index.name = "Rank"

    st.dataframe(rank, use_container_width=True)
