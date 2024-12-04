# 🎯 Option Pricing Models: A Web App for European Option Pricing

Welcome to the **Option Pricing Models** repository! This project is a simple yet powerful web app for calculating **European option prices** using three popular financial models:

- 🧮 **Black-Scholes Model**  
- 🎲 **Monte Carlo Simulation**  

Each model is interactive, customizable, and visualized through an intuitive **Streamlit web interface**. The app fetches live stock price data from Yahoo Finance, processes it, and calculates the **call** and **put** option prices based on user inputs.

---

## 🔧 Features

1. **Option Pricing Models**  
   Calculate option prices using these three approaches:
   - **Black-Scholes Model**: Analytically calculates prices using a closed-form formula.
   - **Monte Carlo Simulation**: Generates thousands of random price paths to compute average payoffs.

2. **Customizable Parameters**  
   Users can input parameters such as:
   - **Ticker**: Stock ticker symbol (e.g., `AAPL`).
   - **Strike Price**: The exercise price of the option.
   - **Expiry Date**: The date on which the option matures.
   - **Risk-Free Rate**: The interest rate for risk-free investments.
   - **Volatility**: The standard deviation of the stock's returns.

3. **Live Data Fetching**  
   - Fetches the latest spot price for any stock using **Yahoo Finance**.
   - Data caching is implemented using `requests-cache` to optimize repeated requests.

4. **Interactive Web App**  
   - A clean and modern interface built with **Streamlit**.
   - Visualizes the results with real-time stock charts and simulated price paths.

---

## 🚀 Live Demo

### Black-Scholes Model:
![Black-Scholes Model Demo](demo/black_scholes_demo.gif)

### Monte Carlo Simulation:
![Monte Carlo Simulation Demo](demo/monte_carlo_demo.gif)

---

## 🗂 Project Structure

Here's how the repository is organized:

