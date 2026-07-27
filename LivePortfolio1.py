
import streamlit as st
import pandas as pd

# Page Configuration (Sets the tab title and icon)
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# --- CUSTOM CSS FOR STYLING ---
# Students can change the hex codes below to match their style!
st.markdown("""
<style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #1E3A8A; /* Navy Blue Accent */
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 20px;
        color: #4B5563; /* Grey text */
        text-align: center;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p class="main-title">👋 Hi, I\'m Student Name!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Artificial Intelligence Student | Problem Solver | Tech Enthusiast</p>', unsafe_allow_html=True)

# Profile layout using columns
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # A placeholder profile image or avatar
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col2:
    st.write("📍 **Location:** Khobar, Saudi Arabia")
    st.write("📧 **Email:** student@example.com")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/yourusername](https://linkedin.com)")
    st.write("💻 **GitHub:** [github.com/yourusername](https://github.com)")

st.write("---")

# --- NAVIGATION SIDEBAR / RADIO TABS ---
# Let them choose which page of your portfolio to look at
page = st.sidebar.radio("Navigate Portfolio", ["About Me", "My Projects", "Interactive Skills Check"])

# ==================== PAGE 1: ABOUT ME ====================
if page == "About Me":
    st.header("🏫 Education")
    st.markdown("""
    **B.S. in Artificial Intelligence**  
    *Imam Abdulrahman Bin Faisal University* | Expected Graduation: 2027
    """)

    st.header("💼 Experience / Co-op")
    st.markdown("""
    **AI Developer Intern** | *Tech Corp* (Summer 2026)  
    - Developed and optimized machine learning models using Python.
    - Collaborated with cross-functional teams to design interactive analytics interfaces.
    """)

# ==================== PAGE 2: PROJECTS ====================
elif page == "My Projects":
    st.header("📁 Featured Projects")

    # Project 1 Layout
    st.subheader("🤖 Smart IoT Strawberry Greenhouse (Wareef)")
    st.write("""
    *An AI- and IoT-driven smart system designed for precision agricultural monitoring.*
    - Built interactive status widgets mapping out temperature, humidity, and optimal cultivation metrics.
    - **Tech Stack:** Streamlit, Python, IoT Sensors, Pandas.
    """)
    if st.button("Launch Wareef Project Demo"):
        st.success("Redirecting to project repository... (Or trigger a balloon animation!)")
        st.balloons()

    st.write("---")

    # Project 2 Layout
    st.subheader("🧁 DELIRIOUS Confectionery Cloud-Store Dashboard")
    st.write("""
    *An interactive business analytics tool tracking cookie sales and ingredient pricing variables.*
    - Integrated dynamic sliders to help planners simulate confectionery profit margins.
    - **Tech Stack:** Python, Streamlit, Plotly Express.
    """)

# ==================== PAGE 3: INTERACTIVE GAME ====================
elif page == "Interactive Skills Check":
    st.header("🛠️ Interactive Skill Matcher")
    st.write("Recruiters: Adjust the sliders below to see if my skills match your requirements!")

    # Interactive widget inputs
    python_needed = st.slider("Required Python Proficiency Level", 1, 10, 5)
    ai_needed = st.slider("Required Machine Learning Proficiency Level", 1, 10, 5)

    # Simple logic responding to inputs
    my_python_skill = 8
    my_ai_skill = 7

    if python_needed <= my_python_skill and ai_needed <= my_ai_skill:
        st.success("🎉 **It's a Match!** My skills exceed your requirements. Let's build something together!")
    else:
        st.warning("⚠️ Some of my skills are still growing, but I'm a fast learner! Let's connect.")
