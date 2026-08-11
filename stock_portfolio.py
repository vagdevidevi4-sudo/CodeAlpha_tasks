import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "NFLX": 470
}


def get_portfolio():
    portfolio = {}

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

    print("\nEnter stock name and quantity (type 'done' to finish)\n")

    while True:
        stock_name = input("Enter stock symbol: ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print(f" '{stock_name}' not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print(" Please enter a valid number.\n")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f" Added {quantity} share(s) of {stock_name}.\n")

    return portfolio


def calculate_investment(portfolio):
    investment_details = []
    total_investment = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        investment_details.append((stock, quantity, price, value))

    return investment_details, total_investment


def display_summary(investment_details, total_investment):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for stock, quantity, price, value in investment_details:
        print(f"{stock:<8}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total_investment}")
    print("=" * 45)


def save_to_file(investment_details, total_investment):
    choice = input("\nDo you want to save the result? (yes/no): ").strip().lower()

    if choice not in ("yes", "y"):
        print("Result not saved.")
        return

    file_format = input("Save as .txt or .csv? ").strip().lower()

    if file_format == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity, price, value in investment_details:
                writer.writerow([stock, quantity, price, value])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print(f" Saved to {filename}")

    elif file_format == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, mode="w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 45 + "\n")
            for stock, quantity, price, value in investment_details:
                f.write(f"{stock:<8}{quantity:<8}${price:<9}${value:<9}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total_investment}\n")
        print(f"Saved to {filename}")

    else:
        print(" Invalid format. File not saved.")


def main():
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    investment_details, total_investment = calculate_investment(portfolio)
    display_summary(investment_details, total_investment)
    save_to_file(investment_details, total_investment)


if __name__ == "__main__":
    main()
