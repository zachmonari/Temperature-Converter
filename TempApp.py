# fancy_temperature_converter_app.py
import streamlit as st

# ---------- Conversion Functions ----------
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


# ---------- Page Styling ----------
st.set_page_config(page_title="🌡️ Temperature Converter", page_icon="🔥", layout="centered")

# Custom CSS for background and text
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #6dd5fa, #2980b9);
        color: blue;
    }
    .stButton>button {
        background-color: #ff7f50;
        color: blue;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #e74c3c;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- UI ----------
st.image("https://cdn-icons-png.flaticon.com/512/1684/1684375.png", width=120)  # thermometer icon
st.title("🌡️ Temperature Converter")
st.write("Convert between **Celsius, Fahrenheit, and Kelvin** with style 🎨")

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

# Convert on button click
if st.button("Convert Temperature"):
    if conversion == "Celsius → Fahrenheit":
        result = celsius_to_fahrenheit(temp)
        st.success(f"🔥 {temp} °C = {result:.2f} °F")

    elif conversion == "Fahrenheit → Celsius":
        result = fahrenheit_to_celsius(temp)
        st.success(f"❄️ {temp} °F = {result:.2f} °C")

    elif conversion == "Celsius → Kelvin":
        result = celsius_to_kelvin(temp)
        st.success(f"🌍 {temp} °C = {result:.2f} K")

    elif conversion == "Kelvin → Celsius":
        result = kelvin_to_celsius(temp)
        st.success(f"🌡️ {temp} K = {result:.2f} °C")

    elif conversion == "Fahrenheit → Kelvin":
        result = fahrenheit_to_kelvin(temp)
        st.success(f"🌍 {temp} °F = {result:.2f} K")

    elif conversion == "Kelvin → Fahrenheit":
        result = kelvin_to_fahrenheit(temp)
        st.success(f"🔥 {temp} K = {result:.2f} °F")

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:black;'>"
    "© 2025 Zach Techs | Made with ❤️ in Streamlit"
    "</div>",
    unsafe_allow_html=True
)

