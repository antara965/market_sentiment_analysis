# Market Sentiment vs Trader Behavior



Objective

Analyze how Bitcoin market sentiment (Fear vs Greed) affects trader performance and behavior on Hyperliquid.



Dataset

\- Bitcoin Fear/Greed Index

\- Hyperliquid Trading Data



Methodology

\- Data cleaning and preprocessing

\- Feature engineering (PnL, win rate, trade frequency, etc.)

\- Sentiment-based comparison

\- Segment analysis



Key Insights



1\. From the PnL distribution plot



\- Most traders cluster around near-zero PnL

\- A few extreme values (both positive \& negative) dominate

\- This pattern exists across all sentiment types



Hence, profitability is not uniform; a small number of traders (likely high-volume or skilled traders) drive most profits and losses.



2\. Comparing Fear vs Greed:



\- No clear shift in median PnL across sentiment types

\- Large variance exists in all conditions

Market sentiment alone does not guarantee profitability. Trader skill and strategy play a larger role than sentiment.



3\. From the win rate plot:

\- Extreme Greed shows slightly higher median win rate

\- Extreme Fear shows lower win rate

Traders tend to win more often in bullish (Greed) conditions, likely due to trending markets.



4\. From the num\_trades plot:

\- Higher number of trades in Fear and Neutral periods

\- Large outliers (overtrading behavior)

Traders tend to overtrade during uncertain or volatile conditions (Fear), possibly trying to recover losses or react to rapid price movements.



5\. From avg\_size plot:

\- Larger trade size outliers in Fear periods

\- More aggressive positioning

Traders take larger, riskier positions during Fear, indicating emotional or reactive trading behavior.





Strategy Recommendations



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



How to Run

1\. Install dependencies:

&nbsp;  pip install pandas numpy matplotlib seaborn scikit-learn



2\. Open notebook:

&nbsp;  jupyter notebook analysis.ipynb

