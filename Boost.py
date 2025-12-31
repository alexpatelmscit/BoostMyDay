import streamlit as st
import random
import io
from datetime import datetime

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Daily Momentum Agent", page_icon="⚡", layout="wide")

# ---------------------------
# Version stamp (helps you verify deployments)
# ---------------------------
APP_VERSION = "v1.3 - CSS via .stApp + .block-container + cards"
st.caption(f"Build: {APP_VERSION} | Loaded at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ---------------------------
# Strong CSS targeting Streamlit DOM
# ---------------------------
st.markdown("""
    <style>
    /* Target the whole app container */
    .stApp {
        background: linear-gradient(180deg, #f6f7fb 0%, #ffffff 100%);
        font-family: "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
    }
    /* The main content container (padding/width area) */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }
    /* Headings */
    .block-container h1 {
        color: #ff4b4b;
        text-align: center;
        letter-spacing: 0.5px;
    }
    .block-container h2 {
        color: #2f2f2f;
        margin: 0.2rem 0 0.8rem 0;
        font-weight: 700;
    }
    /* Card layout */
    .card {
        background: #ffffff;
        border-radius: 14px;
        padding: 16px 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        border: 1px solid #eef0f4;
        height: 100%;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #1f2937;
    }
    .card ul {
        margin: 0;
        padding-left: 18px;
    }
    .card li {
        margin: 6px 0;
    }
    /* Buttons */
    .stButton>button {
        border-radius: 10px;
        background: #ff4b4b;
        color: #fff;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(255,75,75,0.3);
    }
    .stButton>button:hover {
        background: #ff6b6b;
    }
    /* Success banner */
    .stSuccess {
        border-left: 4px solid #10b981;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Title and intro
# ---------------------------
st.title("⚡ Daily Momentum Picks")
st.write("Click Shuffle for fresh energy boosters. Save or Share your set to lock in momentum.")

# ---------------------------
# Data pools
# ---------------------------
motivations_pool = [
    "Believe in progress, not perfection.",
    "Consistency beats intensity — small steps daily build greatness.",
    "Your energy creates your reality — protect it fiercely.",
    "Discipline is choosing what you want most over what you want now.",
    "Momentum builds when you act, not when you wait.",
    "Do it badly, do it slowly — just do it daily.",
    "You don’t need more time, you need more focus."
]

songs_pool = [
    "Eye of the Tiger – Survivor",
    "Stronger – Kanye West",
    "Don't Stop Me Now – Queen",
    "Happy – Pharrell Williams",
    "On Top of the World – Imagine Dragons",
    "Can't Hold Us – Macklemore & Ryan Lewis",
    "Uptown Funk – Mark Ronson ft. Bruno Mars"
]

exercises_pool = [
    "Jumping jacks (2 minutes)",
    "Push-ups (3 sets of 15)",
    "Plank hold (60 seconds)",
    "Squats (3 sets of 20)",
    "Burpees (10 reps)",
    "Mountain climbers (2 minutes)",
    "Fast walk (10 minutes)"
]

foods_pool = [
    "Greek yogurt with berries",
    "Oatmeal with nuts",
    "Green smoothie (spinach, banana, chia seeds)",
    "Avocado toast",
    "Mixed fruit bowl",
    "Paneer + salad bowl",
    "Sprouts chaat (lemon + onions)"
]

tech_pool = [
    "Learn basics of Docker (containers & images)",
    "Explore Python FastAPI for modern APIs",
    "Understand GitHub Actions for CI/CD pipelines",
    "Build quick dashboards in Streamlit",
    "Review Selenium 4 locator syntax (By.XPATH etc.)",
    "Try pytest parameterization & fixtures",
    "Automate small tasks with Makefiles"
]

habits_pool = [
    "Morning journaling (5 minutes reflection)",
    "Daily 20-minute reading habit",
    "Digital detox: 1 hour no screens before bed",
    "Gratitude list before sleep (3 wins)",
    "Plan tomorrow’s top 3 tasks each evening",
    "Pomodoro: 25/5 cycles x 4",
    "Hydration target: 8 glasses tracked"
]

# ---------------------------
# Helper
# ---------------------------
def pick_three(pool):
    return random.sample(pool, 3)

# ---------------------------
# Controls
# ---------------------------
col_left, col_right = st.columns([1, 1])
with col_left:
    shuffle = st.button("🔄 Shuffle Picks")
with col_right:
    st.write("")  # spacing

# ---------------------------
# Generate picks (fresh every run or shuffle)
# ---------------------------
picks = {
    "💡 Motivations": pick_three(motivations_pool),
    "🎵 Songs": pick_three(songs_pool),
    "🏋️ Exercises": pick_three(exercises_pool),
    "🥗 Diet Foods": pick_three(foods_pool),
    "💻 Tech Info": pick_three(tech_pool),
    "📖 Habits": pick_three(habits_pool),
}

# ---------------------------
# Display cards in a grid
# ---------------------------
grid = list(picks.items())
for i in range(0, len(grid), 3):
    row = grid[i:i+3]
    cols = st.columns(len(row))
    for (category, items), c in zip(row, cols):
        with c:
            # Card with title + list
            st.markdown(f"<div class='card'><div class='card-title'>{category}</div>", unsafe_allow_html=True)
            st.markdown("<ul>", unsafe_allow_html=True)
            for item in items:
                # Add category-specific icons inline
                if "Motivations" in category:
                    icon = "💡"
                elif "Songs" in category:
                    icon = "🎵"
                elif "Exercises" in category:
                    icon = "🏋️"
                elif "Diet Foods" in category:
                    icon = "🥗"
                elif "Tech Info" in category:
                    icon = "💻"
                else:
                    icon = "📖"
                st.markdown(f"<li>{icon} {item}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)

# ---------------------------
# Save & Share
# ---------------------------
buffer = io.StringIO()
for category, items in picks.items():
    buffer.write(f"{category}:\n")
    for item in items:
        buffer.write(f"- {item}\n")
    buffer.write("\n")
txt_data = buffer.getvalue()

st.success("⚡ Stay consistent — small daily wins compound into unstoppable momentum!")

dl_col, share_col = st.columns([1, 2])
with dl_col:
    st.download_button(
        label="💾 Save My Picks (TXT)",
        data=txt_data,
        file_name="daily_momentum_picks.txt",
        mime="text/plain"
    )
with share_col:
    st.text_area("📤 Share My Picks", txt_data, height=160)
    st.info("Copy and share via WhatsApp, Email, Slack, or anywhere you like.")
