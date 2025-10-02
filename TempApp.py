# temperature_converter_app.py
import streamlit as st

# Conversion functions
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


# Streamlit UI
st.title("🌡️ Temperature Converter")

# Choose conversion
conversion = st.selectbox(
    "Choose a conversion",
    (
        "Celsius → Fahrenheit",
        "Fahrenheit → Celsius",
        "Celsius → Kelvin",
        "Kelvin → Celsius",
        "Fahrenheit → Kelvin",
        "Kelvin → Fahrenheit",
    )
)

# Input value
temp = st.number_input("Enter temperature:", value=0.0)

# Convert when button pressed
if st.button("Convert"):
    if conversion == "Celsius → Fahrenheit":
        result = celsius_to_fahrenheit(temp)
        st.success(f"{temp} °C = {result:.2f} °F")

    elif conversion == "Fahrenheit → Celsius":
        result = fahrenheit_to_celsius(temp)
        st.success(f"{temp} °F = {result:.2f} °C")

    elif conversion == "Celsius → Kelvin":
        result = celsius_to_kelvin(temp)
        st.success(f"{temp} °C = {result:.2f} K")

    elif conversion == "Kelvin → Celsius":
        result = kelvin_to_celsius(temp)
        st.success(f"{temp} K = {result:.2f} °C")

    elif conversion == "Fahrenheit → Kelvin":
        result = fahrenheit_to_kelvin(temp)
        st.success(f"{temp} °F = {result:.2f} K")

    elif conversion == "Kelvin → Fahrenheit":
        result = kelvin_to_fahrenheit(temp)
        st.success(f"{temp} K = {result:.2f} °F")


# Add your sign/trademark
st.markdown("---")
st.caption("© 2025 Zach Techs | Temperature Converter App")
