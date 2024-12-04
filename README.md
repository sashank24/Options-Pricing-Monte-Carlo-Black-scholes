# Option Pricing Web Application 📊

A simple and intuitive **web application** for calculating **European Option Prices** using two powerful models:
- **Black-Scholes Model**
- **Monte Carlo Simulation**

The app fetches **real-time stock data** from Yahoo Finance to make accurate predictions and provides an interactive user interface built using **Streamlit**.

---

## 🔑 Key Features
1. **Option Pricing Models**:
   - **Black-Scholes Model**: A closed-form solution for European options based on analytical formulas.
   - **Monte Carlo Simulation**: A probabilistic model simulating thousands of possible outcomes to estimate option prices.
   
2. **Real-Time Data Integration**:
   - Fetches historical stock prices from **Yahoo Finance** (e.g., Open, High, Low, Close) using the `yfinance` library.

3. **Interactive User Interface**:
   - Built with **Streamlit** for an engaging, user-friendly experience.
   - Dynamic input fields and visualizations for easy parameter tuning and decision-making.

4. **Custom Visualizations**:
   - Plots historical stock prices.
   - Displays simulated stock price movements for Monte Carlo models.

5. **Performance Optimization**:
   - Caches data using Streamlit to minimize redundant API calls and improve efficiency.

---

## 📂 Project Structure

```plaintext
option-pricing-models/
├── option_pricing/
│   ├── __init__.py              # Package initializer
│   ├── base.py                  # Abstract base class for option pricing models
│   ├── BlackScholesModel.py     # Black-Scholes implementation
│   ├── MonteCarloSimulation.py  # Monte Carlo Simulation implementation
│   ├── ticker.py                # Fetch and manage Yahoo Finance data
├── streamlit_app.py             # Streamlit web application
├── option_pricing_test.py       # Testing script for models and data
├── Requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration for containerized deployment
├── README.md                    # Project documentation
