"""
AI response formatting utilities.
"""

import re


def format_coach_response(raw: str) -> str:
    """
    Clean and format Gemini coaching response for display.
    Removes leading/trailing whitespace and normalises markdown.
    """
    # Strip extra blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", raw.strip())
    return cleaned


def format_report(raw: str, date: str) -> str:
    """
    Format AI weekly report with a header and dividers for download.
    """
    header = f"Life-OS AI – Weekly Wellness Report\nGenerated: {date}\n{'=' * 45}\n\n"
    return header + raw.strip()


def build_accountability_link(base_url: str, total_minutes: int) -> str:
    """
    Build a shareable URL with screen time embedded as a query param.
    """
    return f"{base_url}?screen={total_minutes}"
