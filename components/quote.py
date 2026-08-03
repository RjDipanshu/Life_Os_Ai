"""
Quote component — motivational quote of the day.
"""

import streamlit as st
import random


QUOTES = [
    ("The key is not to prioritise what's on your schedule, but to schedule your priorities.", "Stephen Covey"),
    ("Your future is created by what you do today, not tomorrow.", "Robert Kiyosaki"),
    ("Focus is the art of knowing what to ignore.", "James Clear"),
    ("Almost everything will work again if you unplug it for a few minutes, including you.", "Anne Lamott"),
    ("Productivity is never an accident. It is always the result of a commitment to excellence.", "Paul J. Meyer"),
    ("You do not rise to the level of your goals. You fall to the level of your systems.", "James Clear"),
    ("The successful warrior is the average man, with laser-like focus.", "Bruce Lee"),
    ("Time is the scarcest resource; unless it is managed, nothing else can be managed.", "Peter Drucker"),
    ("It's not about having time, it's about making time.", "Unknown"),
    ("Digital minimalism is about being intentional with technology.", "Cal Newport"),
]


def render_quote():
    """Render a random daily motivational quote in a styled callout."""

    quote, author = random.choice(QUOTES)  # noqa: S311

    st.markdown(
        f"""<div style="background: linear-gradient(135deg, #667eea22, #764ba222); border-left: 4px solid #667eea; border-radius: 8px; padding: 16px 20px; margin: 12px 0;">
<p style="font-size:1rem; font-style:italic; margin:0; color: inherit;">&ldquo;{quote}&rdquo;</p>
<p style="font-size:0.85rem; margin:8px 0 0 0; color:gray;">— {author}</p>
</div>""",
        unsafe_allow_html=True,
    )
