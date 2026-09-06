# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}
portfolio = {}
total_investment = 0
print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))
# Number of stocks to enter
n = int(input("Enter number of different stocks: "))
for i in range(n):
    stock = input(f"\nEnter stock name {i + 1}: ").upper()
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        investment = stock_prices[stock] * quantity
        portfolio[stock] = quantity
        total_investment += investment
        print(f"Price of {stock}: ${stock_prices[stock]}")
        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not available in the list.")
# Display portfolio
print("\n===== PORTFOLIO SUMMARY =====")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")
print(f"\nTotal Investment Value: ${total_investment}")
# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n"
        )
    file.write(f"\nTotal Investment Value: ${total_investment}")
print("\nPortfolio saved successfully to portfolio.txt")
