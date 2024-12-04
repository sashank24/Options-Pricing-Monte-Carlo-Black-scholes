# Standart python imports
from enum import Enum
from datetime import datetime, timedelta

# Third party imports
import streamlit as st

# Local package imports
from option_pricing import BlackScholesModel, MonteCarloPricing, Ticker

# Adding custom styles
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom, #2c3e50, #4ca1af);
        color: white;
    }
    h1 {
        font-size: 3rem;
        color: #e74c3c;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #34495e;
        color: white;
    }
    .css-1v0mbdj, .css-znku1x {
        color: white !important;
    }
    .stButton > button {
        background-color: #e74c3c;
        color: white;
        font-size: 1rem;
        border-radius: 5px;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #c0392b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

data = Ticker.get_historical_data('AAPL')
if data is None:
    print("Failed to fetch data.")
else:
    print(data.head())


class OPTION_PRICING_MODEL(Enum):
    BLACK_SCHOLES = 'Black Scholes Model'
    MONTE_CARLO = 'Monte Carlo Simulation'

@st.cache_data
def get_historical_data(ticker):
    """Getting historical data for speified ticker and caching it with streamlit app."""
    return Ticker.get_historical_data(ticker)

# Ignore the Streamlit warning for using st.pyplot()
# st.set_option('deprecation.showPyplotGlobalUse', False)

# Main title
st.title('Option pricing')

# User selected model from sidebar 
st.sidebar.title("Select Pricing Method")
pricing_method = st.sidebar.radio('Please select option pricing method', options=[model.value for model in OPTION_PRICING_MODEL])

# Display selected model in a styled format
st.subheader(f"📊 Pricing Method: {pricing_method}")

# Define Enum
class OPTION_PRICING_MODEL(Enum):
    BLACK_SCHOLES = "Black Scholes Model"
    MONTE_CARLO = "Monte Carlo Simulation"


# Cache function for fetching data
@st.cache_data
def get_historical_data(ticker):
    """Getting historical data for specified ticker and caching it."""
    return Ticker.get_historical_data(ticker)


# Dynamic UI layout
if pricing_method == OPTION_PRICING_MODEL.BLACK_SCHOLES.value:
    st.markdown("### 🎯 Parameters for Black-Scholes Model")
    
    col1, col2 = st.columns(2)
    with col1:
        ticker = st.text_input("📈 Ticker Symbol:", "AAPL", help="Enter the stock ticker (e.g., AAPL).")
        strike_price = st.number_input("💲 Strike Price:", min_value=0, value=300)
        exercise_date = st.date_input(
            "📅 Exercise Date:",
            min_value=datetime.today() + timedelta(days=1),
            value=datetime.today() + timedelta(days=365),
        )
    with col2:
        risk_free_rate = st.slider("💵 Risk-Free Rate (%):", 0, 100, 10)
        sigma = st.slider("📊 Volatility (Sigma, %):", 0, 100, 20)

    if st.button(f"📈 Calculate Option Price for {ticker}"):
        st.spinner("Fetching data and calculating prices...")
        data = get_historical_data(ticker)

        if data is None or data.empty:
            st.error(f"Failed to fetch data for ticker '{ticker}'. Please check the ticker symbol.")
        else:
            st.success(f"✅ Data fetched successfully for {ticker}!")
            st.write(data.tail())
            Ticker.plot_data(data, ticker, "Close")
            st.pyplot()

            # Black-Scholes Calculation
            spot_price = Ticker.get_last_price(data, "Close")
            days_to_maturity = (exercise_date - datetime.now().date()).days
            risk_free_rate = risk_free_rate / 100
            sigma = sigma / 100

            # Option pricing
            BSM = BlackScholesModel(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma)
            call_price = BSM.calculate_option_price("Call Option")
            put_price = BSM.calculate_option_price("Put Option")

            st.subheader(f"📈 Call Option Price: {call_price:.2f}")
            st.subheader(f"📉 Put Option Price: {put_price:.2f}")

elif pricing_method == OPTION_PRICING_MODEL.MONTE_CARLO.value:
    st.markdown("### 🎲 Parameters for Monte Carlo Simulation")
    
    ticker = st.text_input("📈 Ticker Symbol:", "AAPL", help="Enter the stock ticker (e.g., AAPL).")
    strike_price = st.number_input("💲 Strike Price:", min_value=0, value=300)
    exercise_date = st.date_input(
        "📅 Exercise Date:",
        min_value=datetime.today() + timedelta(days=1),
        value=datetime.today() + timedelta(days=365),
    )
    risk_free_rate = st.slider("💵 Risk-Free Rate (%):", 0, 100, 10)
    sigma = st.slider("📊 Volatility (Sigma, %):", 0, 100, 20)
    num_simulations = st.slider("🌀 Number of Simulations:", min_value=100, max_value=100000, value=10000)

    if st.button(f"🎲 Run Monte Carlo Simulation for {ticker}"):
        with st.spinner("Running simulations..."):
            data = get_historical_data(ticker)

            if data is None or data.empty:
                st.error(f"Failed to fetch data for ticker '{ticker}'. Please check the ticker symbol.")
            else:
                st.success(f"✅ Data fetched successfully for {ticker}!")
                st.write(data.tail())
                Ticker.plot_data(data, ticker, "Close")
                st.pyplot()

                # Monte Carlo Calculation
                spot_price = Ticker.get_last_price(data, "Close")
                days_to_maturity = (exercise_date - datetime.now().date()).days
                risk_free_rate = risk_free_rate / 100
                sigma = sigma / 100

                # Run simulation
                MC = MonteCarloPricing(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, num_simulations)
                MC.simulate_prices()
                call_price = MC.calculate_option_price("Call Option")
                put_price = MC.calculate_option_price("Put Option")

                st.subheader(f"📈 Call Option Price: {call_price:.2f}")
                st.subheader(f"📉 Put Option Price: {put_price:.2f}")
                st.markdown("### 🌀 Simulated Price Movements")
                MC.plot_simulation_results(50)
                st.pyplot()
