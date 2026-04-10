# Crypto Trader Behavior Analysis Using Market Sentiment

 Live Dashboard: (https://market-sentiment-analysis.streamlit.app/) or (https://market-sentiment-app-baewgzhdcxedfefc.centralindia-01.azurewebsites.net/)



## Objective

The objective is to understand how trader performance, risk-taking, and behavior vary across different emotional market conditions such as **Fear** and **Greed**.



## Dataset

\- Bitcoin Fear/Greed Index

\- Hyperliquid Trading Data



## Methodology

\- Data cleaning and preprocessing

\- Feature engineering (PnL, win rate, trade frequency, etc.)

\- EDA

\- Statistical Analysis

\- Clustering



## Insights
- Trader behavior varies significantly with market sentiment  
- Increased trading activity does not always improve profitability  
- Larger position sizes combined with frequent trading increase risk  
- Distinct trader groups exist based on behavioral patterns 

- A few extreme values (both positive \& negative) dominate

## Strategy Recommendations

1\. Avoid overtrading during Fear

Traders significantly increase trading frequency during Fear periods, often leading to poor decision-making.

2\. Reduce position size during Fear

Larger trade sizes during Fear indicate increased risk-taking, which may lead to larger losses.

3\. Follow trend during Greed

Higher win rates in Greed periods suggest that trending markets are easier to trade.

4\. Avoid emotional "buy the dip" trades

Increased long bias during Fear suggests traders are prematurely entering long positions.

5\. Focus on consistency over high-risk trades

Profitability is driven by a few extreme outcomes rather than consistent gains.

## How to Run

1\. Install dependencies:

&nbsp;  pip install pandas numpy matplotlib seaborn scikit-learn



2\. Open notebook:

&nbsp;  jupyter notebook analysis.ipynb

