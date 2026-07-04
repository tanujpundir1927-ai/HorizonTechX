def stock_tracker():
    # Hardcoded dictionary for stock prices
    prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 350, "AMZN": 130}
    portfolio = {}
    
    print("Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN")
    
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        
        if stock in prices:
            try:
                quantity = int(input(f"Enter quantity for {stock}: "))
                portfolio[stock] = portfolio.get(stock, 0) + quantity
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Stock not found in database.")
            
    total_value = 0
    print("\n--- Your Portfolio ---")
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            value = qty * prices[stock]
            total_value += value
            output_str = f"{stock}: {qty} shares @ ${prices[stock]} = ${value}"
            print(output_str)
            file.write(output_str + "\n")
            
        print(f"\nTotal Investment Value: ${total_value}")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    
    print("Results saved in portfolio_summary.txt")

if __name__ == "__main__":
    stock_tracker()