import streamlit as st

# Page configuration
st.set_page_config(page_title="Interactive Quiz", page_icon="💡", layout="centered")

st.title("💡 Quick Interactive Knowledge Check")
st.write("Answer the 5 questions below using different interactive widgets to test your knowledge!")

# Initialize score counter
score = 0

st.write("---")

# ==================== QUESTION 1: NUMBER INPUT (MATH) ====================
st.subheader("Question 1: Math Puzzle")
q1_input = st.number_input(
    "What is the result of:  13 + 13 × 0 + 13 ?",
    value=None,
    step=1,
    key="q1"
)

if q1_input is not None:
    # Order of operations (PEMDAS): 13 * 0 = 0 -> 13 + 0 + 13 = 26
    if q1_input == 26:
        st.success("✅ Correct! Remember order of operations (multiplication first): 13 + 0 + 13 = 26.")
        score += 1
    else:
        st.error("❌ Incorrect. Hint: Multiply before adding!")

st.write("---")

# ==================== QUESTION 2: RADIO BUTTONS ====================
st.subheader("Question 2: Web Frameworks")
q2_input = st.radio(
    "Which Python library allows you to build data apps without frontend experience?",
    options=["Select an option...", "Django", "Streamlit", "Flask", "FastAPI"],
    key="q2"
)

if q2_input != "Select an option...":
    if q2_input == "Streamlit":
        st.success("✅ Correct! Streamlit makes web dev simple using pure Python.")
        score += 1
    else:
        st.error("❌ Not quite. Try another framework!")

st.write("---")

# ==================== QUESTION 3: SELECTBOX DROPDOWN ====================
st.subheader("Question 3: Version Control")
q3_input = st.selectbox(
    "Which command-line tool is used to track changes in source code?",
    options=["Select an option...", "Docker", "Git", "Pip", "Conda"],
    key="q3"
)

if q3_input != "Select an option...":
    if q3_input == "Git":
        st.success("✅ Correct! Git tracks code history across developers.")
        score += 1
    else:
        st.error("❌ Incorrect. Try again!")

st.write("---")

# ==================== QUESTION 4: SLIDER ====================
st.subheader("Question 4: Default Port")
q4_input = st.slider(
    "On which port number does a Streamlit app run locally by default?",
    min_value=8000,
    max_value=9000,
    value=8000,
    step=1,
    key="q4"
)

# Button to confirm slider selection
if st.button("Submit Question 4 Answer"):
    if q4_input == 8501:
        st.success("✅ Spot on! Port 8501 is Streamlit's default local port.")
        score += 1
    else:
        st.error(f"❌ {q4_input} is incorrect. Hint: It starts with 85..")

st.write("---")

# ==================== QUESTION 5: TEXT INPUT ====================
st.subheader("Question 5: Cloud Hosting")
q5_input = st.text_input(
    "Which cloud platform lets you store code repositories and run Codespaces?",
    key="q5"
)

if q5_input:
    if q5_input.strip().lower() == "github":
        st.success("✅ Correct! GitHub hosts repositories and cloud environments.")
        score += 1
    else:
        st.error("❌ Keep trying!")

st.write("---")

# ==================== SCOREBOARD & CELEBRATION ====================
st.markdown(f"### 📊 Final Score: **{score} / 5**")

if score == 5:
    st.balloons()
    st.info("🎉 Perfect Score! You've mastered all 5 questions!")
elif score >= 3:
    st.snow()
    st.info("👍 Great effort! You passed the check.")
