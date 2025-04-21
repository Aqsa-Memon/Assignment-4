import streamlit as st

# App title
st.title("💪 Body Mass Index (BMI) Calculator")

# Subtitle
st.markdown("Use this calculator to check your BMI and understand your body health category. 🧠")

# Input sliders
height = st.slider("📏 Enter your height (in cm):", 100, 250, 170)
weight = st.slider("⚖️ Enter your weight (in kg):", 30, 200, 70)

# BMI calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI result
st.subheader(f"🧮 Your BMI is: **{bmi:.2f}**")

# Category detection
st.markdown("### 🗂️ BMI Category")

if bmi < 18.5:
    st.warning("🍃 **Underweight** – Consider gaining some healthy weight. Eat well and take care! 💚")
elif 18.5 <= bmi < 25:
    st.success("✅ **Normal weight** – Great job! Maintain your healthy lifestyle. 🥗🏃‍♂️")
elif 25 <= bmi < 30:
    st.info("⚠️ **Overweight** – A little more exercise might help! You’ve got this! 💪")
else:
    st.error("🚨 **Obesity** – Consider consulting a healthcare professional for guidance. ❤️‍🩹")

# BMI category guide
with st.expander("📘 What is BMI?"):
    st.markdown("""
    - 🍃 **Underweight**: BMI less than 18.5  
    - ✅ **Normal weight**: BMI between 18.5 and 24.9  
    - ⚠️ **Overweight**: BMI between 25 and 29.9  
    - 🚨 **Obesity**: BMI 30 or greater  
    """)
