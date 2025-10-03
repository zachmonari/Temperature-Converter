#temperature_converter_app.py
import streamlit as st


# ---------- Conversion Functions ----------
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(temp):
    return (temp - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

# ---------- Page Styling ----------
st.set_page_config(page_title="🌡️ Temperature Converter", page_icon="🔥", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #6dd5fa, #2980b9);
        color: white;
    }
    /* Buttons */
    .stButton>button {
        background-color: #ff7f50;
        color: white;
        border-radius: 12px;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e74c3c;
        transform: scale(1.05);
    }
    /* Footer */
    .footer {
        text-align:center;
        color: black;
        font-size: 14px;
        padding-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Initialize Session State ----------
if "conversion_log" not in st.session_state:
    st.session_state.conversion_log = []

# ---------- UI ----------
st.image("https://cdn-icons-png.flaticon.com/512/1684/1684375.png", width=120)
st.title("🌡️ Temperature Converter")
st.write("Convert between **Celsius, Fahrenheit, and Kelvin** with style 🎨🔥❄️")

# Dropdown for conversion
conversion = st.selectbox(
    "Choose a conversion type:",
    (
        "Celsius → Fahrenheit",
        "Fahrenheit → Celsius",
        "Celsius → Kelvin",
        "Kelvin → Celsius",
        "Fahrenheit → Kelvin",
        "Kelvin → Fahrenheit",
    )
)

# Input temperature
temp = st.number_input("Enter the temperature value:", value=0.0)
msg=None
# Convert on button click
if st.button("Convert Temperature"):
    if conversion == "Celsius → Fahrenheit":
        result = celsius_to_fahrenheit(temp)
        msg = f"🔥 {temp} °C = {result:.2f} °F"
    elif conversion == "Fahrenheit → Celsius":
        result = fahrenheit_to_celsius(temp)
        msg = f"❄️ {temp} °F = {result:.2f} °C"
    elif conversion == "Celsius → Kelvin":
        result = celsius_to_kelvin(temp)
        msg = f"🌍 {temp} °C = {result:.2f} K"
    elif conversion == "Kelvin → Celsius":
        result = kelvin_to_celsius(temp)
        msg = f"🌡️ {temp} K = {result:.2f} °C"
    elif conversion == "Fahrenheit → Kelvin":
        result = fahrenheit_to_kelvin(temp)
        msg = f"🌍 {temp} °F = {result:.2f} K"
    elif conversion == "Kelvin → Fahrenheit":
        result = kelvin_to_fahrenheit(temp)
        msg = f"🔥 {temp} K = {result:.2f} °F"

    # show result
    st.success(msg)
    # Save to history
    st.session_state.conversion_log.append(msg)

# ---------- Show History ----------
if st.session_state.conversion_log:
    st.subheader("📝 Conversion History")
    for i, entry in enumerate(st.session_state.conversion_log, start=1):
        st.write(f"{i}. {entry}")

# ---------- Footer ----------
st.markdown("---", unsafe_allow_html=True)
st.markdown(
    "<div class='footer'>© 2025 <b>Zach Techs™</b> | Made with ❤️ in Streamlit</div>",
    unsafe_allow_html=True
)

