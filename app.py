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

# Streamlit Page Config
st.set_page_config("📊 AI Stock Market Insight", layout="wide", page_icon="📈")

st.markdown("<div class='title'>📊 AI-Powered Stock Market Insight Dashboard</div>", unsafe_allow_html=True)

# Input section
symbol = st.text_input("Enter a Stock Symbol (e.g., AAPL, TSLA, MSFT)").upper()
years = st.slider("Select historical data duration (in years)", min_value=1, max_value=10, value=5)

# Symbol validation
if symbol:
    if not is_valid_symbol(symbol):
        st.error(f"❌ Symbol '{symbol}' is not valid. Please enter a correct USA stock symbol.")
        st.stop()

    stock_name = get_stock_name(symbol)
    st.subheader(f"📈 Historical Data for {stock_name} ({symbol})")

    # Load and plot historical data
    data = get_historical_data(symbol, years=years)
    st.line_chart(data['Close'])

    # Current price
    live_price = get_live_price(symbol)
    st.write(f"💰 Current Price: **${live_price:.2f}**")

    # AI Prediction
    with st.spinner("🔮 Predicting next price using Gemini AI..."):
        predicted_price = get_price_prediction(symbol, data)
        st.success(f"📉 Predicted Price (Next Day): **${predicted_price}**")

    # AI Recommendation
    with st.spinner("🤖 AI Recommending an Action..."):
        recommendation = get_recommendation(symbol, data)
        st.markdown(f"### 🔁 Recommendation: {recommendation}")

    # AI Peer Suggestions
    with st.spinner("🔍 Suggesting peer companies using Gemini AI..."):
        peers = get_peers(symbol, stock_name)
        st.markdown("### 🧑‍🤝‍🧑 Suggested Peers")
        st.text(peers)
