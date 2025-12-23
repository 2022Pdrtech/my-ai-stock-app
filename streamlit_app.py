import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock App")
st.title("My Stock Advisor")

tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOGL"]

for ticker in tickers:
    try:
        data = yf.Ticker(ticker).history(period="60d")
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            avg_price = data['Close'].mean()

            st.write(f"### {ticker}")
            st.write(f"Price: ${current_price:.2f}")

            if current_price < avg_price:
                st.success("SUGGESTION: BUY")
            else:
                st.info("SUGGESTION: WAIT")
            st.divider()
    except Exception as e:
        st.error(f"Error loading {ticker}")
