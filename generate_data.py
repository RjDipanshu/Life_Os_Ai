import pandas as pd
import random
from datetime import datetime, timedelta
import os

# -----------------------------
# App Categories
# -----------------------------
apps = {
    "Coding": ["VS Code", "IntelliJ IDEA", "GitHub Desktop"],
    "Education": ["Chrome", "ChatGPT", "Coursera"],
    "Social Media": ["Instagram", "Facebook", "X"],
    "Entertainment": ["YouTube", "Netflix", "Prime Video"],
    "Communication": ["WhatsApp", "Gmail"],
    "Music": ["Spotify"],
    "Productivity": ["Notion", "Google Calendar"]
}

# -----------------------------
# Date Range (Last 14 Days)
# -----------------------------
today = datetime.today()
start_date = today - timedelta(days=13)

rows = []

for i in range(14):
    current_date = start_date + timedelta(days=i)

    weekday = current_date.weekday()

    # Weekdays = More productive
    if weekday < 5:
        usage = {
            "Coding": random.randint(120, 240),
            "Education": random.randint(40, 100),
            "Social Media": random.randint(20, 70),
            "Entertainment": random.randint(30, 80),
            "Communication": random.randint(20, 60),
            "Music": random.randint(10, 40),
            "Productivity": random.randint(20, 60),
        }

    # Weekends = More entertainment
    else:
        usage = {
            "Coding": random.randint(20, 80),
            "Education": random.randint(10, 50),
            "Social Media": random.randint(70, 180),
            "Entertainment": random.randint(100, 220),
            "Communication": random.randint(30, 80),
            "Music": random.randint(40, 120),
            "Productivity": random.randint(10, 40),
        }

    for category, total_minutes in usage.items():

        app = random.choice(apps[category])

        rows.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "App_Name": app,
            "Category": category,
            "Minutes_Used": total_minutes
        })

df = pd.DataFrame(rows)

os.makedirs("data", exist_ok=True)

df.to_csv("data/screentime.csv", index=False)

print("[OK] Dataset generated successfully!")
print(df.head())
