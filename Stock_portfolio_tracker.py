# Stock Portfolio Tracker
# Predefined stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}
total_investment = 0
portfolio = {}
print("📊 Stock Portfolio Tracker")
while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stocks:
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            
            value = quantity * stocks[stock_name]
            total_investment += value

            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

            print(f"{stock_name} value: {value}")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("Stock not found in list!")
# Display portfolio summary
print("\n📁 Your Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock} : {qty} shares")
print("\n💰 Total Investment Value:", total_investment)
# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Your Portfolio:\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} : {qty} shares\n")
    file.write(f"\nTotal Investment: {total_investment}")

print("\nData saved to portfolio.txt")