# Stock Price Analyzer

- Pulls real historical stock data using the yfinance library and analyzes it with pandas

## Features
- Average, highest, and lowest closing price
- Daily price changes and biggest single-day gain/loss
- Daily returns and market volatility
- Rolling averages and returns across multiple timeframes (1 day, 7 day, 1 month, 3 month, 6 month, 1 year)
- A line chart of closing price over time

## How to run
1. Make sure Python is installed
2. Install dependencies: `pip install yfinance pandas matplotlib seaborn`
3. Run: `python "Stock price analyzer.py"`
4. Follow the on-screen prompts

## What I learned
- Working with real external data via an API (yfinance), instead of static datasets
- Multi-index column selection in pandas (e.g. 'data["Close", ticker]')
- Returning multiple values from a function using tuples

