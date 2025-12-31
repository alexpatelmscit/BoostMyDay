import streamlit as st
import random
import io

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="Daily Momentum Agent", page_icon="⚡", layout="wide")

# 🎨 Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    h2 {
        color: #333333;
        margin-top: 20px;
    }
    .category-box {
        background: #ffffff;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Title
# ---------------------------
st.title("⚡ Daily Momentum Picks")
st.write("Click *Shuffle* to refresh your energy boosters anytime, and *Save/Share My Picks* to keep them!")

# ---------------------------
# Pools of Options
# ---------------------------
motivations_pool = [
    "Believe in progress, not perfection.",
    "Consistency beats intensity — small steps daily build greatness.",
    "Your energy creates your reality — protect it fiercely.",
    "Discipline is choosing what you want most over what you want now.",
    "Momentum builds when you act, not when you wait."
]

songs_pool = [
    "🎵 Eye of the Tiger – Survivor",
    "🎵 Stronger – Kanye West",
    "🎵 Don't Stop Me Now – Queen",
    "🎵 Happy – Pharrell Williams",
    "🎵 On Top of the World – Imagine Dragons"
]

exercises_pool = [
    "🏋️ Jumping jacks (2 minutes)",
    "🏋️ Push-ups (3 sets of 15)",
    "🏋️ Plank hold (60 seconds)",
    "🏋️ Squats (3 sets of 20)",
    "🏋️ Burpees (10 reps)"
]

foods_pool = [
    "🥗 Greek yogurt with berries",
    "🥗 Oatmeal with nuts",
    "🥗 Green smoothie (spinach, banana, chia seeds)",
    "🥗 Avocado toast",
    "🥗 Mixed fruit bowl"
]

tech_pool = [
    "💻 Learn basics of Docker for containerization",
    "💻 Explore Python’s FastAPI for modern APIs",
    "💻 Understand GitHub Actions for CI/CD automation",
    "💻 Experiment with Streamlit for quick dashboards",
    "💻 Review Selenium 4 syntax for modern automation"
]

habits_pool = [
    "📖 Morning journaling (5 minutes reflection)",
    "📖 Daily 20-minute reading habit",
    "📖 Digital detox: 1 hour no screens before bed",
    "📖 Gratitude list before sleep",
    "📖 Plan tomorrow’s top 3 tasks each evening"
]

# ---------------------------
# Helper Function
# ---------------------------
def pick_three(pool):
    return random.sample(pool, 3)

# ---------------------------
# Shuffle Button
# ---------------------------
if st.button("🔄 Shuffle Picks"):
    st.session_state["shuffle"] = True

# ---------------------------
# Generate Picks
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
# Display Sections
# ---------------------------
output = io.StringIO()
for category, items in picks.items():
    st.markdown(f"<div class='category-box'><h2>{category}</h2>", unsafe_allow_html=True)
    for item in items:
        st.write(f"- {item}")
    st.markdown("</div>", unsafe_allow_html=True)

    output.write(f"{category}:\n")
    for item in items:
        output.write(f"- {item}\n")
    output.write("\n")

st.success("⚡ Stay consistent — small daily wins compound into unstoppable momentum!")

# ---------------------------
# Save & Share My Picks
# ---------------------------
txt_data = output.getvalue()

st.download_button(
    label="💾 Save My Picks (TXT)",
    data=txt_data,
    file_name="daily_momentum_picks.txt",
    mime="text/plain"
)

st.text_area("📤 Share My Picks", txt_data, height=200)
st.info("Copy the text above and share it via WhatsApp, Email, or any platform you like!")
