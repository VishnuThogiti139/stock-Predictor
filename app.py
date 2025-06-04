import streamlit as st
from services.data_loader import (
    get_historical_data,
    get_live_price,
    get_stock_name,
    is_valid_symbol,
)
from services.stock_info import (
    get_price_prediction,
    get_recommendation,
    get_peers,
)

st.set_page_config("📊 AI-Powered Stock Insight", layout="wide", page_icon="📈")
st.markdown("<h1 class='title'>📊 AI-Powered Stock Market Insight Dashboard</h1>", unsafe_allow_html=True)

symbol = st.text_input("Enter a Stock Symbol (e.g., AAPL, TSLA, MSFT)").upper()
years = st.slider("Select historical data duration (in years)", min_value=1, max_value=10, value=5)

if symbol:
    stock_name = get_stock_name(symbol)
    if "❌ Invalid" in stock_name:
        st.error(f"Symbol '{symbol}' is not valid. Please enter a correct 'USA' stock symbol.")
        st.stop()
    st.subheader(f"📈 Historical Data for {stock_name} ({symbol})")
    data = get_historical_data(symbol, years=years)
    st.line_chart(data['Close'])

    live_price = get_live_price(symbol)
    st.write(f"💰 Current Price: **${live_price:.2f}**")

    with st.spinner("🔮 Predicting next price..."):
        predicted_price = get_price_prediction(symbol, data)
        st.success(f"📉 Predicted Price: **${predicted_price.strip()}**")

    with st.spinner("🤖 AI Recommending an Action..."):
        recommendation = get_recommendation(symbol, data)
        st.markdown(f"### 🔁 Recommendation: {recommendation}")

    with st.spinner("🔍 Fetching peers using Gemini AI..."):
        peers = get_peers(symbol, stock_name)
        st.markdown("### 🏷 Suggested Peers")
        st.text(peers)
