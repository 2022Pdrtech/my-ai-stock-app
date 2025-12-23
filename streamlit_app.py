import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Page Setup
st.set_page_config(page_title="AI Stock Advisor", layout="wide")
st.title("📈 My AI Stock Advisor")
st.write(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# 1. The List of Stocks (You can change these symbols)
tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOGL"]

# 2. The Logic Engine
def analyze_stocks():
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            # Pull 60 days of history
            hist = stock.history(period="60d")
            
            if hist.empty:
                st.error(f"Could not find data for {ticker}")
                continue

            current_price = hist['Close'].iloc[-1]
            avg_price = hist['Close'].mean()
            
            # Layout the UI
            with st.container():
                st.subheader(f"Stock: {ticker}")
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.metric("Live Price", f"${current_price:.2f}")
                    # Prediction Logic
                    if current_price < (avg_price * 0.98):
                        st.success("🔥 SIGNAL: BUY NOW")
                        st.write("Reason: Price is significantly lower than recent average.")
                    elif current_price > (avg_price * 1.05):
                        st.warning("⚠️ SIGNAL: SELL / HOLD")
                        st.write("Reason: Price is currently peaking.")
                    else:
                        st.info("⚖️ SIGNAL: NEUTRAL")
                        st.write("Reason: Price is stable.")

                with col2:
                    # Visual Chart
                    fig = go.Figure(data=[go.Candlestick(
                        x=hist.index,
                        open=hist['Open'], high=hist['High'],
                        low=hist['Low'], close=hist['Close']
                    )])
                    fig.update_layout(height=250, margin=dict(l=0,r=0,b=0,t=0), template="plotly_dark")
                    st.plotly_chart(fig, use_container_width=True)
                
                st.divider()
        except Exception as e:
            st.error(f"Error loading {ticker}: {e}")

# Run the app
analyze_stocks()
