import streamlit as st
import yfinance as yf

st.set_page_config(page_title="SafeOption AI", page_icon="🛡️")

st.title("SafeOption AI")
st.subheader("Education First. Risk First.")

st.write(
    "This demo helps beginner investors understand the basic risk structure of selling put options."
)

st.warning(
    "Educational demo only. This tool does not provide financial advice or execute trades."
)

st.sidebar.header("Input Parameters")

stock_symbol = st.sidebar.text_input("Stock Symbol", "IBM")

try:
    ticker = yf.Ticker(stock_symbol)
    live_price = ticker.history(period="1d")["Close"].iloc[-1]
except:
    live_price = 210.0

current_price = st.sidebar.number_input(
    "Current Stock Price",
    min_value=0.0,
    value=float(round(live_price, 2))
)
strike_price = st.sidebar.number_input("Strike Price", min_value=0.0, value=200.0)
premium = st.sidebar.number_input("Premium Received", min_value=0.0, value=2.50)
days_to_expiry = st.sidebar.number_input("Days to Expiry", min_value=1, value=7)
ex_dividend = st.sidebar.selectbox(
    "Ex-Dividend Before Expiry?",
    ["No", "Yes"]
)

dividend_amount = st.sidebar.number_input(
    "Dividend Amount",
    min_value=0.0,
    value=0.0
)

earnings_event = st.sidebar.selectbox(
    "Earnings Before Expiry?",
    ["No", "Yes"]
)
contracts = st.sidebar.number_input("Number of Contracts", min_value=1, value=1)

break_even = strike_price - premium
max_exposure = (strike_price * 100 * contracts) - (premium * 100 * contracts)
premium_yield = premium / strike_price if strike_price > 0 else 0
annualized_return = premium_yield * (365 / days_to_expiry)

distance_to_strike = (current_price - strike_price) / current_price if current_price > 0 else 0

if distance_to_strike > 0.10:
    assignment_risk = "Low"
elif distance_to_strike > 0.03:
    assignment_risk = "Moderate"
else:
    assignment_risk = "High"

st.header("Sell Put Risk Analysis")

st.write(f"### Stock: {stock_symbol}")

col1, col2 = st.columns(2)

with col1:
    st.metric("Break-even Price", f"${break_even:.2f}")
    st.metric("Maximum Exposure", f"${max_exposure:,.2f}")

with col2:
    st.metric("Premium Yield", f"{premium_yield * 100:.2f}%")
    st.metric("Estimated Annualized Return", f"{annualized_return * 100:.2f}%")

st.header("Risk Warnings")

if assignment_risk == "Low":
    st.success(f"Assignment Risk: {assignment_risk}")
elif assignment_risk == "Moderate":
    st.warning(f"Assignment Risk: {assignment_risk}")
else:
    st.error(f"Assignment Risk: {assignment_risk}")

st.info(
    "Selling puts may result in stock assignment. Users should only sell puts on stocks they are willing to own."
)

st.header("Educational Notes")

st.write(
    """
    **What is a Sell Put?**

    Selling a put option means you receive a premium, but you may be required to buy the stock at the strike price if the option is assigned.

    **Key Risks:**

    - The stock price may fall below the strike price.
    - You may be assigned and required to buy shares.
    - Earnings events and high volatility can increase risk.
    - Dividend dates may affect assignment behavior.

    **SafeOption Principle:**

    Learn the risk before seeking the return.
    """
)
