import streamlit as st
import pandas as pd
import numpy as np

# ==================== PAGE CONFIGURATION ====================
# 🎨 CHALLENGE 1: Change the title, icon, or layout!
st.set_page_config(
    page_title="Chaos Control Center 🌀", 
    page_icon="⚡", 
    layout="centered"
)

# ==================== CUSTOM CSS / THEME OVERRIDE ====================
# 🎨 CHALLENGE 2: Change these hex codes to your favorite wild colors!
st.markdown("""
<style>
    /* Change the background color of the main page */
    .stApp {
        background-color: #F0F4F8;
    }
    
    /* Style the header title */
    .main-header {
        color: #FF4B4B;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        border-bottom: 3px dashed #FF4B4B;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<p class="main-header">🚨 The Break-The-Interface Challenge 🚨</p>', unsafe_allow_html=True)
st.write("Modify this code to make it as chaotic, colorful, or personalized as possible!")

st.write("---")

# ==================== CELEBRATION BUTTON ====================
# 🎈 CHALLENGE 3: Customize the button label or swap st.balloons() with st.snow()!
st.subheader("1️⃣ The Big Red Button")
if st.button("🎉 DO NOT PRESS THIS BUTTON!"):
    st.balloons()
    st.success("You broke the rules! Enjoy the balloons 🎈")

st.write("---")

# ==================== FUNNY SLIDER METRICS ====================
# 📊 CHALLENGE 4: Rename these sliders to track something funny!
# Examples: "Hours of sleep" vs "Cups of coffee", or "Stress level" vs "Cat videos watched"
st.subheader("2️⃣ Personal Reality Meter")

col1, col2 = st.columns(2)

with col1:
    stat_a = st.slider("☕ Cups of Coffee Consumed Today", min_value=0, max_value=15, value=3)

with col2:
    stat_b = st.slider("😴 Hours of Sleep Last Night", min_value=0, max_value=12, value=4)

# Dynamic reaction logic based on their sliders
if stat_a > stat_b:
    st.warning("⚠️ Warning: Coffee intake exceeds sleep hours! System operating on pure adrenaline.")
elif stat_b >= 8:
    st.info("😴 Well rested! You might actually survive today's workshop.")
else:
    st.error("💥 Critical error: Battery low, send snacks!")

st.write("---")

# ==================== RANDOM DATA CHART ====================
# 📈 CHALLENGE 5: Change column names or adjust graph dimensions!
st.subheader("3️⃣ Completely Unnecessary Live Chart")

# Generate random chaotic data
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["Panic Level 😱", "Motivation 🚀"]
)

st.line_chart(chart_data)
