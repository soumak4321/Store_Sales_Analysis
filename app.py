
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Store Sales Analysis")

df = pd.read_csv("superstore.csv", encoding='latin1')

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Total Sales")
st.write(df['Sales'].sum())

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,5))

top_products.plot(kind='bar', ax=ax)

plt.title("Top 10 Products")

st.pyplot(fig)
