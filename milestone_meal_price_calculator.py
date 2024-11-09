# Import necessary library for currency formatting
import locale

# Function to calculate change and display it in a formatted way
def calculate_change(total_cost, amount_given, currency_symbol='$'):
    # Ensure two decimal places for inputs
    total_cost = round(float(total_cost), 2)
    amount_given = round(float(amount_given), 2)

    # Calculate the change
    change = round(amount_given - total_cost, 2)

    # Check if the customer gave enough money
    if change < 0:
        print(f"Not enough money. You're short by {currency_symbol}{abs(change):.2f}.")
        return
    
    # Display total cost, amount given, and change with proper formatting
    print(f"Total Cost: {currency_symbol}{total_cost:.2f}")
    print(f"Amount Given: {currency_symbol}{amount_given:.2f}")
    print(f"Change: {currency_symbol}{change:.2f}")
    
    # Additional Feature: Break down change into denominations
    breakdown_change(change, currency_symbol)

# Function to break down change into common denominations
def breakdown_change(change, currency_symbol='$'):
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    print("\nBreakdown of change:")
    
    for denom in denominations:
        count = int(change // denom)
        if count > 0:
            print(f"{count} x {currency_symbol}{denom:.2f}")
        change = round(change % denom, 2)

# Main function for user input
def main():
    # User inputs
    currency_symbol = input("Enter the currency symbol (e.g., $, €, £): ")
    total_cost = float(input(f"Enter the total cost ({currency_symbol}): "))
    amount_given = float(input(f"Enter the amount given ({currency_symbol}): "))

    # Call the function to calculate change
    calculate_change(total_cost, amount_given, currency_symbol)

# Run the main function
if __name__ == "__main__":
    main()