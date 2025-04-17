import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit App
st.set_page_config(page_title="Data Dashboard", page_icon="📊")
st.title("📊 Streamlit Crash Course Dashboard")

st.header("Upload Your CSV or Use Demo Data")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using demo data.")
    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Values": [10, 20, 30, 40]
    })

st.subheader("Data Preview")
st.dataframe(df)

st.subheader("Bar Chart Visualization")

if "Category" in df.columns and "Values" in df.columns:
    fig = px.bar(df, x="Category", y="Values", title="Category vs Values")
    st.plotly_chart(fig)
else:
    st.warning("Make sure your data has 'Category' and 'Values' columns for plotting.")

st.subheader("Simple Filters")
selected_column = st.selectbox("Select Column to View", df.columns)

st.dataframe(df[[selected_column]])

st.markdown("---")
st.caption("Made with ❤️ using Streamlit, Pandas, and Plotly")
