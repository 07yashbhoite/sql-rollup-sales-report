import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Report Generator", layout="centered")

st.title("📊 Sales Report Using SQL ROLLUP")
st.markdown("Upload your sales CSV file to visualize total sales by category.")

uploaded_file = st.file_uploader("Upload your Sales.csv file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Show data
    st.subheader("📋 Sample Sales Data")
    st.dataframe(df.head())

    # Group by category
    category_totals = df.groupby("ProductCategory")["SaleAmount"].sum().sort_values()

    # Plot
    st.subheader("📈 Total Sales by Product Category")
    fig, ax = plt.subplots(figsize=(8, 5))
    category_totals.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_xlabel("Total Sales (₹)")
    ax.set_ylabel("Product Category")
    ax.set_title("Total Sales by Category")
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig)

    # Summary
    st.markdown(f"### 🧾 Grand Total Sales: ₹ {df['SaleAmount'].sum():,.2f}")
