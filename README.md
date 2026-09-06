# 📊 Stock Portfolio Tracker
A simple **Python-based Stock Portfolio Tracker** developed as part of the **CodeAlpha Internship – Task 2**.
## 📌 Project Description
This project allows users to enter stock names and the number of shares they own. It calculates the investment value for each stock and the **total portfolio investment** using predefined stock prices.

The stock prices are stored in a Python dictionary.
## ✨ Features
* Enter the number of different stocks
* Enter stock names and quantities
* Uses predefined stock prices
* Calculates individual stock investment
* Calculates total investment value
* Displays a portfolio summary
* Saves the portfolio summary to a `portfolio.txt` file
## 🛠️ Technologies Used
* **Python**
* Dictionaries
* User Input / Output
* Arithmetic Operations
* File Handling
## 📈 Sample Stock Prices
| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| GOOGL |  $140 |
| MSFT  |  $420 |
| AMZN  |  $185 |
> Note: These are hardcoded sample prices for educational purposes and are not live market prices.
## ▶️ How to Run
1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:
```bash
python stock_portfolio_tracker.py
```
6. Enter the stock names and quantities when prompted.
## 💻 Example
```text
===== STOCK PORTFOLIO TRACKER =====
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
Enter number of different stocks: 2
Enter stock name 1: AAPL
Enter quantity of AAPL: 
Price of AAPL: $180
Investment in AAPL: $900
Enter stock name 2: TSLA
Enter quantity of TSLA: 2
Price of TSLA: $250
Investment in TSLA: $500
===== PORTFOLIO SUMMARY =====
AAPL: 5 shares × $180 = $900
TSLA: 2 shares × $250 = $500
Total Investment Value: $1400
Portfolio saved successfully to portfolio.txt
```
## 📁 Project Files
```text
CodeAlpha_-StockPortfolioTracker-
│
├── stock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```
## 🎯 Learning Outcomes
Through this project, I practiced:
* Python dictionaries
* Loops
* Conditional statements
* User input
* Arithmetic calculations
* File handling
* Git and GitHub
## 👨‍💻 Internship
**CodeAlpha Internship – Task 2**
### Stock Portfolio Tracker
This project was created for educational and internship purposes.
## ⚠️ Disclaimer
This project does not use real-time stock market data. The prices are manually defined in the Python program and are intended only for learning purposes.
