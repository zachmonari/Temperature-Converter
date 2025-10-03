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

# --- UI ---
st.image("https://cdn-icons-png.flaticon.com/512/1048/1048947.png", width=120)
st.title("🎲 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it? 🤔")

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

# Restart game
if st.button("🔄 Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.won = False
    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:black;'>© 2025 Zach Techs | Made with ❤️ in Streamlit</div>",
    unsafe_allow_html=True
)
