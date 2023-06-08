# Stock-Alerts
Stock Alerts is a Python-based project that leverages an API to monitor stock prices and provide desktop notifications when the ticker prices reach predefined thresholds. It empowers users to stay informed about the latest developments in the stock market and make timely decisions.

## Features
Real-Time Stock Price Monitoring: The project uses the yfinance library to fetch the last adjusted close price for each stock ticker in real-time, ensuring up-to-date information.

![Modules](https://github.com/TalLovton/Stock-Alerts/assets/78549129/a0dc9bc5-c4a7-48cc-8767-a34cd366b6e6)

![Terminal](https://github.com/TalLovton/Stock-Alerts/assets/78549129/0cd8f0bd-b550-4918-92dd-8300a71addc3)

![Alerts](https://github.com/TalLovton/Stock-Alerts/assets/78549129/e187a7a6-6b96-495b-91a6-112ccf2c7b31)

Customizable Alert System: Users can set their desired entry and take profit prices for each stock, enabling personalized and targeted notifications.

Desktop Notifications: The Plyer library is integrated to display desktop notifications when a stock price surpasses the specified thresholds. The notifications include relevant details such as the ticker symbol, current price, and suggested actions (e.g., buying or selling).

User-Friendly Menu: The project provides an interactive menu that allows users to easily add, edit, and remove stock tickers from the monitoring list. It ensures a seamless and intuitive user experience.


Input Validation: The program performs validation checks to ensure that the user's input for entry and take profit prices is valid, enhancing data integrity and reliability.

## Prerequisites
Python 3.x

yfinance library: Install using pip install yfinance.

Plyer library: Install using pip install plyer.

## Getting Started
1. Clone this repository: git clone https://github.com/yourusername/stock-alerts.git

2. Install the required libraries: pip install -r requirements.txt

3. Run the stockAlarm.py script: python stockAlarm.py

4. Follow the on-screen prompts to set up your stock alerts and monitor prices.
## Usage
Upon running the script, you will be prompted to enter a stock ticker, take profit price, and entry price. Follow the instructions to input the desired information.

The program will continuously monitor the stock prices and display them along with the corresponding ticker symbol.

When a stock price exceeds the defined thresholds, a desktop notification will be displayed, suggesting appropriate actions based on the current price.

Use the provided menu options to add, edit, or remove stock tickers as needed.
