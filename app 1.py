
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📈 Sales Dashboard")

st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Country",
    ["Saudi Arabia", "UAE", "Qatar"]
)

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", "$52K", "+12%")
col2.metric("Orders", "1,240", "+6%")
col3.metric("Customers", "320", "+9%")

data = pd.DataFrame(
    np.random.randn(50, 2),
    columns=["Sales", "Profit"]
)

left, right = st.columns(2)

with left:
    st.line_chart(data)

with right:
    st.bar_chart(data)

st.dataframe(data)
