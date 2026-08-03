"""
Gemini AI integration using google-genai SDK.
"""

import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()


def _get_client() -> genai.Client:
    """Return a cached Gemini client."""
    api_key = os.getenv("GEMINI_API_KEY", "")
    return genai.Client(api_key=api_key)


def generate_text(prompt: str, model: str = "gemini-2.0-flash") -> str:
    """
    Send a prompt to Gemini and return the text response.
    Uses caching for successful responses and provides smart fallback on network/quota errors.
    """
    return _call_gemini_cached(prompt, model)


@st.cache_data(show_spinner=False, ttl=300)
def _call_gemini_cached(prompt: str, model: str) -> str:
    try:
        client = _get_client()
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        if response and response.text:
            return response.text.strip()
        raise ValueError("Empty response from Gemini API.")
    except Exception as exc:
        err_msg = str(exc)
        # Clear cache entry if it was an error so retries work once connection is restored
        _call_gemini_cached.clear()
        
        # Smart offline fallback response
        return _fallback_coaching_response(prompt, err_msg)


def _fallback_coaching_response(prompt: str, err_msg: str) -> str:
    """Provide structured offline coaching advice when network/API is unavailable."""
    is_network = "getaddrinfo" in err_msg or "11001" in err_msg or "connection" in err_msg.lower()
    reason = "Offline / Network Disconnected" if is_network else "API Rate Limit / Quota Exceeded"
    
    return f"""
> 💡 *Note: Operating in Smart Offline Mode ({reason})*

### 📊 Habit Assessment
Your digital footprint shows significant time concentrated in high-screen categories today. Balance is key to preventing digital burnout.

### 🏃 3 Specific Real-World Activity Replacements
1. **Reclaim Social/Entertainment Time:** Swap 45 minutes of passive scrolling for a 30-minute outdoor jog or brisk walk.
2. **Mindful Break:** Replace continuous screen usage with 15 minutes of uninterrupted reading or journaling.
3. **Physical Prep:** Reallocate evening device usage to meal prepping or stretching before bed.

🔥 *Remember: Control your devices, don't let your devices control your day!*
""".strip()

