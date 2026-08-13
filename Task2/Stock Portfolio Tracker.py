stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_value = 0




print("=== Stock Portfolio Tracker ===")
print("Available stocks and prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: $ {price}")

print("\nEnter your stocks.")
print("Type 'done' when you are finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    value = stock_prices[stock_name] * quantity
    total_value +=value


    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print(f"Investment value: ${value}\n")

    # Display portfolio
print("\n=== Your Portfolio ===")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Save option
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    file_type = input("Choose file type (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio\n")
            file.write("-------------------\n")

            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(
                    f"{stock}: {quantity} shares = ${value}\n")
                file.write(
                    f"\nTotal Investment Value: ${total_value}"
                )

                print("Portfolio saved successfully in portfolio.txt")

    elif file_type == "csv":
        import csv

        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["Stock", "Quantity", "Price", "Total Value"]
            )

            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity

                writer.writerow(
                    [
                        stock,
                        quantity,
                        stock_prices[stock],
                        value
                    ]
                )

                writer.writerow(
                    ["TOTAL", "", "", total_value]
                )

                print("Portfolio saved successfully in portfolio.csv")

    else:
        print("Invalid file type.")

else:
    print("Program finished.")













