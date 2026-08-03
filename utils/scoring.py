"""
Productivity scoring utilities.
"""

import pandas as pd

PRODUCTIVE_CATEGORIES = {"Coding", "Education", "Productivity"}
NEUTRAL_CATEGORIES = {"Communication", "Finance"}
DRAINING_CATEGORIES = {"Social Media", "Entertainment", "Gaming"}


def compute_productivity_score(day_df: pd.DataFrame) -> int:
    """
    Calculate a 0-100 productivity score for the day.
    """

    productive = day_df[
        day_df["Category"].isin(PRODUCTIVE_CATEGORIES)
    ]["Minutes_Used"].sum()

    neutral = day_df[
        day_df["Category"].isin(NEUTRAL_CATEGORIES)
    ]["Minutes_Used"].sum()

    draining = day_df[
        day_df["Category"].isin(DRAINING_CATEGORIES)
    ]["Minutes_Used"].sum()

    raw = productive * 0.5 + neutral * 0.1 - draining * 0.3

    return int(max(0, min(100, raw)))


def screen_time_status(total_minutes: int) -> tuple[str, str]:
    """
    Return (status_label, emoji) based on total daily screen time.
    """

    if total_minutes < 240:
        return "Excellent Digital Balance", "🎉"

    elif total_minutes < 360:
        return "Moderate Usage", "👍"

    else:
        return "High Screen Time", "🚨"


def weekly_streak(df: pd.DataFrame, daily_goal: int) -> int:
    """
    Count consecutive days where total usage was under the daily goal.
    """

    daily_totals = (
        df.groupby("Date")["Minutes_Used"]
        .sum()
        .sort_index(ascending=False)
    )

    streak = 0

    for minutes in daily_totals:
        if minutes <= daily_goal:
            streak += 1
        else:
            break

    return streak


def calculate_scores(day_df: pd.DataFrame, daily_goal: int) -> dict:
    """
    Returns dashboard scores.
    """

    total = int(day_df["Minutes_Used"].sum())

    productivity = compute_productivity_score(day_df)

    if daily_goal > 0:
        wellness = max(
            0,
            min(
                100,
                round(
                    100 - abs(total - daily_goal) / daily_goal * 100
                ),
            ),
        )
    else:
        wellness = 100

    return {
        "productivity": productivity,
        "wellness": wellness,
        "total": total,
    }