# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("ABC Manufacturing - Demand Forecast Visualization")

# Tạo dữ liệu
np.random.seed(42)
weeks = list(range(1, 157))
base_demand = np.random.normal(loc=200, scale=20, size=156).astype(int)
price = np.random.choice([9.5, 10, 10.5], size=156)
promo = np.random.choice([0, 1], size=156, p=[0.7, 0.3])
adjusted_demand = base_demand + (promo * np.random.randint(10, 30, size=156))

df = pd.DataFrame({
    'Week': weeks,
    'Demand': adjusted_demand,
    'Price': price,
    'Promo': promo
})

st.subheader("📈 Sample Data (First 10 Rows)")
st.dataframe(df.head(10))

# Vẽ biểu đồ
st.subheader("📊 Data Visualizations")

# 1. Line Chart - Demand Over Time
st.markdown("**1. Weekly Product Demand Over 3 Years**")
fig1, ax1 = plt.subplots()
sns.lineplot(x='Week', y='Demand', data=df, ax=ax1)
ax1.set_title("Weekly Product Demand")
st.pyplot(fig1)

# 2. Distribution Histogram
st.markdown("**2. Distribution of Demand**")
fig2, ax2 = plt.subplots()
sns.histplot(df['Demand'], kde=True, bins=20, ax=ax2)
ax2.set_title("Demand Distribution")
st.pyplot(fig2)

# 3. Boxplot: Promo vs Demand
st.markdown("**3. Demand Comparison With/Without Promotion**")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Promo', y='Demand', data=df, ax=ax3)
ax3.set_title("Promotion vs Demand")
st.pyplot(fig3)

# 4. Scatterplot Week vs Demand (colored by Promo)
st.markdown("**4. Weekly Demand Colored by Promotion**")
fig4, ax4 = plt.subplots()
sns.scatterplot(x='Week', y='Demand',
