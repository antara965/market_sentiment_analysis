import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Crypto Trader Dashboard",
    layout="wide"
)

#title
st.title("📊 Crypto Trader Behavior Analysis")
st.markdown("Analyze how trader behavior changes under **Fear vs Greed market conditions**.")

df = pd.read_csv("processed_trader_behavior.csv")

st.markdown("### Filter Data")

sentiment = st.selectbox(
    "Select Market Sentiment",
    df["classification"].unique()
)

filtered_df = df[df["classification"] == sentiment].copy()

st.markdown("---")

st.subheader(" Dataset Preview")
st.dataframe(filtered_df.head())

st.markdown("---")

#metrics
st.subheader(" Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average PnL", round(filtered_df["daily_pnl"].mean(), 2))
col2.metric("Average Trade Size", round(filtered_df["avg_trade_size"].mean(), 2))
col3.metric("Average Win Rate", round(filtered_df["win_rate"].mean(), 2))

st.markdown("---")

st.subheader(" Trading Behavior Analysis")

col1, col2 = st.columns(2)

#profit distribution
with col1:
    st.write("### Profit Distribution")
    st.write("Shows how trader profits vary under selected market sentiment.")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="classification", y="daily_pnl", data=filtered_df, ax=ax)
    st.pyplot(fig)

#trading frequency
with col2:
    st.write("### Trading Frequency")
    st.write("Indicates how actively traders are trading under this sentiment.")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="classification", y="num_trades", data=filtered_df, ax=ax)
    st.pyplot(fig)

st.markdown("---")

st.subheader(" Additional Insights")

col1, col2 = st.columns(2)

#win rate
with col1:
    st.write("### Win Rate Distribution")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="classification", y="win_rate", data=filtered_df, ax=ax)
    st.pyplot(fig)

#risk score
with col2:
    st.write("### Risk Score Analysis")
    st.write("Risk Score = Trade Size × Number of Trades")

    filtered_df["risk_score"] = filtered_df["avg_trade_size"] * filtered_df["num_trades"]

    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="classification", y="risk_score", data=filtered_df, ax=ax)
    st.pyplot(fig)

st.markdown("---")

#cluster analysis
st.subheader(" Trader Segmentation")

st.write("Clusters represent different types of traders based on behavior.")

fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(
    x="avg_trade_size",
    y="win_rate",
    hue="cluster",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

st.markdown("---")

st.subheader(" Top Performing Traders")

top_traders = filtered_df.sort_values(by="daily_pnl", ascending=False).head(10)
st.dataframe(top_traders)

st.markdown("---")

#final insights
st.subheader(" Key Insights")

st.write("""
- Traders tend to show higher profit variability during different market sentiment phases  
- High-frequency trading does not always result in higher win rates  
- Larger trade sizes combined with frequent trading increase overall risk exposure  
- Distinct trader groups exist based on risk-taking behavior and trading patterns  
""")

st.markdown("---")

with st.expander("Key Terms"):
    st.markdown("""
    - **PnL (Profit and Loss):** Total profit or loss made by a trader.
    - **Win Rate:** Percentage of profitable trades.
    - **Trade Size:** Amount used per trade.
    - **Risk Score:** Trade Size × Number of Trades.
    - **Market Sentiment:** Fear (cautious) vs Greed (aggressive).
    - **Cluster:** Groups of traders with similar behavior.
    """)

st.markdown("---")

st.subheader("🔗 Project Links")

st.markdown("""
**GitHub Repository:**  
👉 [View Project Code](https://github.com/antara965/market_sentiment_analysis.git)

**About this Project:**  
This project analyzes how cryptocurrency trader behavior changes based on market sentiment using the Fear & Greed Index and Hyperliquid trading data.

**Created by:**  
Antara Surkule
""")