import streamlit as st
import yfinance as yf
import plotly
import pandas as pd

st.title("🚀 My AI Stock Advisor")
st.write("Checking the market for 'Buy' opportunities...")

# The stocks we want to watch
tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOGL"]

for ticker in tickers:
    # Get the data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="60d")
    
    current_price = hist['Close'].iloc[-1]
    avg_price = hist['Close'].mean()
    
    # Create a nice visual box for each stock
    with st.container():
        st.subheader(f"Stock: {ticker}")
        st.metric("Current Price", f"${current_price:.2f}")
        
        if current_price < avg_price:
            st.success("✅ SUGGESTION: BUY. Price is currently below the 60-day average.")
        else:
            st.info("Wait: Price is higher than average right now.")
        st.divider()
