import streamlit as st
import pandas as pd
import numpy as np

st.title("🚀 My First Cross-Major Streamlit App")
st.write("Welcome! Modify the widgets below to see how interactive web apps work.")

user_name = st.text_input("What is your name?", "Student")
st.subheader(f"Hello, {user_name}! 👋")

number = st.slider("Select a number of data points", 10, 100, 50)

data = pd.DataFrame(
    np.random.randn(number, 2),
    columns=['X Factor', 'Y Factor']
)

st.line_chart(data)
