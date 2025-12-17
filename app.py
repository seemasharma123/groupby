import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.DataFrame({
'Region': ['North', 'South', 'North', 'South', 'East'],
'Sales': [100, 150, 200, 180, 120],
'Orders': [5, 8, 10, 7, 6]
})
total = df.groupby('Region')['Sales'].sum()
print(total)
avg = df.groupby('Region')['Sales'].mean()
summary = df.groupby('Region').agg({
'Sales': ['sum', 'mean', 'count'],
'Orders': 'sum'
})
print(summary)
result = df.groupby('Region')['Sales'].sum().reset_index()
st.title("Sales by Region")
st.write("Total sales by region:")
st.dataframe(result)        # or st.write(result)
st.write("Summary by region:")
st.dataframe(summary)