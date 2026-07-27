import streamlit as st
import pandas as pd
import numpy as np

# ==================== 1. PAGE CONFIGURATION ====================
# 🎨 TEAMS: Edit the title, emoji icon, and layout!
st.set_page_config(
    page_title="My Major's Dream App 🚀",
    page_icon="💡",
    layout="centered"
)

# ==================== 2. CUSTOM THEME / CSS ====================
# 🎨 TEAMS: Customize your background and header colors using Hex codes!
st.markdown("""
<style>
    /* Change main background color */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Custom Title Styling */
    .app-title {
        color: #1E3A8A; /* Change title color here */
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .app-subtitle {
        color: #64748B;
        font-size: 18px;
        text-align: center;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== 3. APP HEADER ====================
# ✏️ TEAMS: Rename your App Title & Subtitle below!
st.markdown('<p class="app-title">🚀 The Ultimate Dream App</p>', unsafe_allow_html=True)
st.markdown('<p class="app-subtitle">Solving real problems with simple Python & Streamlit</p>', unsafe_allow_html=True)

st.write("---")

# ==================== 4. SIDEBAR SETUP ====================
st.sidebar.header("⚙️ Team Settings")
team_name = st.sidebar.text_input("Team / Major Name", "AI Innovators")
st.sidebar.write(f"Developed by: **{team_name}**")

# ==================== 5. INPUT SECTION (3 INPUTS) ====================
st.header("📥 Input Parameters")

col1, col2 = st.columns(2)

# INPUT 1: Slider
with col1:
    # ✏️ TEAMS: Rename this slider label and min/max limits to fit your major!
    input_slider = st.slider(
        "☕ Primary Metric (e.g., Coffee / Stress / Data Points)", 
        min_value=0, 
        max_value=10, 
        value=5
    )

# INPUT 2: Selectbox / Dropdown
with col2:
    # ✏️ TEAMS: Change the dropdown options!
    input_dropdown = st.selectbox(
        "🎯 Select Category / Specialty",
        options=["Option A (Low Risk)", "Option B (Medium Risk)", "Option C (High Risk)"]
    )

# INPUT 3: Text Input / Query
# ✏️ TEAMS: Change the label or placeholder prompt!
input_text = st.text_input(
    "📝 Target Variable / User Input Prompt", 
    placeholder="Type something here..."
)

st.write("---")

# ==================== 6. ACTION & OUTPUT SECTION ====================
st.header("📊 Generated Output & Diagnosis")

# Action Button to generate result
if st.button("🚀 Run Dream Analysis"):
    
    # ✏️ TEAMS: Customize your results and messages!
    st.subheader(f"Results for: '{input_text if input_text else 'Default Query'}'")
    
    # Dynamic Alert box based on slider value
    if input_slider >= 7:
        st.success(f"✅ **Optimal Output Reached!** Metrics are within high performance bounds for {input_dropdown}.")
        st.balloons() # Trigger celebration balloons!
    elif input_slider >= 4:
        st.warning(f"⚠️ **Moderate Status.** Adjust parameters to improve outcomes for {input_dropdown}.")
    else:
        st.error(f"❌ **Action Needed!** Metric level ({input_slider}) is too low.")

    # Output Metric Display
    m1, m2 = st.columns(2)
    m1.metric(label="Calculated Efficiency Score", value=f"{input_slider * 10}%", delta="+5%")
    m2.metric(label="Selected Category", value=input_dropdown.split()[0])

    # Dynamic Data Chart Output
    st.subheader("📈 Trend Visualizer")
    chart_data = pd.DataFrame(
        np.random.randn(10, 2) + [input_slider, input_slider],
        columns=["Target Trend", "Baseline"]
    )
    st.line_chart(chart_data)

else:
    st.info("👆 Adjust your 3 inputs above and click **Run Dream Analysis** to see your app in action!")
