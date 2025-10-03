import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="🎲 Number Guessing Game", page_icon="🎯", layout="centered")

# --- Styling ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    .stButton>button {
        background-color: #ff7f50;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 8px 20px;
    }
    .stButton>button:hover {
        background-color: #e74c3c;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Initialize Session State ---
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.won = False
    st.session_state.mode = "Easy"

# Initialize scoreboard
if "scoreboard" not in st.session_state:
    st.session_state.scoreboard = {
        "Easy 😎": {"Wins": 0, "Losses": 0},
        "Medium 🙂": {"Wins": 0, "Losses": 0},
        "Hard 😱": {"Wins": 0, "Losses": 0},
    }

# --- UI ---
st.image("https://cdn-icons-png.flaticon.com/512/1048/1048947.png", width=120)
st.title("🎲 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it? 🤔")

# Difficulty selection
mode = st.radio("Choose a difficulty mode:", ["Easy 😎", "Medium 🙂", "Hard 😱"])
st.session_state.mode = mode

# Set attempt limits
if mode == "Easy 😎":
    max_attempts = None   # unlimited
elif mode == "Medium 🙂":
    max_attempts = 10
else:
    max_attempts = 7

# Guess input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if not st.session_state.won:
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.warning("📉 Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.info("📈 Too high! Try again.")
        else:
            st.balloons()
            st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.won = True
            st.session_state.scoreboard[mode]["Wins"] += 1

        # Check for max attempts
        if max_attempts and st.session_state.attempts >= max_attempts and not st.session_state.won:
            st.error(f"💀 Game Over! You've used {max_attempts} attempts. The number was {st.session_state.secret_number}.")
            st.session_state.won = True
            st.session_state.scoreboard[mode]["Losses"] += 1

# Restart game
if st.button("🔄 Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.won = False
    st.rerun()

# --- Scoreboard Display ---
st.markdown("---")
st.subheader("📊 Scoreboard")
for m, record in st.session_state.scoreboard.items():
    st.write(f"**{m}** → ✅ Wins: {record['Wins']} | ❌ Losses: {record['Losses']}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:black;'>© 2025 Zach Techs | Made with ❤️ in Streamlit</div>",
    unsafe_allow_html=True
)

