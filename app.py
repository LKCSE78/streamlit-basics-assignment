import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Summary Dashboard")
st.subheader("Filter sales data by category and visualize performance")

# Create hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Tablet", "Jeans"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [1200, 300, 800, 450, 600, 350]
}

df = pd.DataFrame(data)

# Sidebar filter
category_filter = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)

# Filter data
filtered_df = df[df["Category"] == category_filter]

# Display filtered data
st.dataframe(filtered_df)

# Line chart for sales
st.line_chart(filtered_df["Sales"])