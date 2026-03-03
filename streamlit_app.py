# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Care Load Forecast Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Care Load Forecast Dashboard")
st.markdown(
    "This dashboard shows the SARIMA forecast, confidence intervals, and probability of exceeding capacity. "
    "Use filters to explore specific date ranges."
)

# ---------- DUMMY DATA ----------
# Replace this section with your real SARIMA forecast and breach probability data
dates = pd.date_range(start="2026-03-01", periods=30)
breach_df = pd.DataFrame({
    'Forecast': np.random.randint(100, 200, size=30),
    'Lower_CI': np.random.randint(90, 150, size=30),
    'Upper_CI': np.random.randint(150, 210, size=30),
    'Breach_Probability': np.random.rand(30)
}, index=dates)

# ---------- METRICS ----------
st.subheader("⚡ Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Max Forecast", f"{breach_df['Forecast'].max():.0f}")
col2.metric("Max Breach Probability", f"{breach_df['Breach_Probability'].max()*100:.1f}%")
col3.metric("Average Forecast", f"{breach_df['Forecast'].mean():.1f}")

# ---------- DATE FILTER ----------
st.subheader("📅 Filter by Date")
start_date = st.date_input("Start Date", breach_df.index.min())
end_date = st.date_input("End Date", breach_df.index.max())
filtered_df = breach_df.loc[start_date:end_date]

st.dataframe(filtered_df.style.background_gradient(subset=['Breach_Probability'], cmap='Reds'))

# ---------- FORECAST PLOT ----------
st.subheader("📈 Forecast with 95% Confidence Interval")
fig, ax = plt.subplots(figsize=(12,5))
sns.set_style("whitegrid")
ax.plot(filtered_df.index, filtered_df['Forecast'], label='Forecast', color='dodgerblue', marker='o')
ax.fill_between(filtered_df.index, filtered_df['Lower_CI'], filtered_df['Upper_CI'], color='dodgerblue', alpha=0.2, label='95% CI')
ax.set_ylabel("Care Load")
ax.set_xlabel("Date")
ax.set_title("Forecast with Confidence Interval")
ax.legend()
st.pyplot(fig)

# ---------- BREACH PROBABILITY PLOT ----------
st.subheader("🔥 Probability of Capacity Breach")
fig2, ax2 = plt.subplots(figsize=(12,4))
ax2.bar(filtered_df.index, filtered_df['Breach_Probability']*100, color='salmon', alpha=0.7)
ax2.axhline(80, color='black', linestyle='--', label='High Risk Threshold (80%)')
ax2.set_ylabel("Probability (%)")
ax2.set_xlabel("Date")
ax2.set_title("Breach Probability")
ax2.legend()
st.pyplot(fig2)

# ---------- HIGHLIGHT TOP 5 RISK DAYS ----------
st.subheader("⚠️ Top 5 High Risk Days")
top5 = filtered_df.sort_values('Breach_Probability', ascending=False).head(5)
st.table(top5.style.format({
    'Forecast': "{:.0f}",
    'Lower_CI': "{:.0f}",
    'Upper_CI': "{:.0f}",
    'Breach_Probability': "{:.1%}"
}).background_gradient(subset=['Breach_Probability'], cmap='Reds'))

# ---------- DOWNLOAD BUTTON ----------
st.subheader("💾 Download Forecast Data")
csv = filtered_df.to_csv().encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='forecast_breach.csv',
    mime='text/csv'
)