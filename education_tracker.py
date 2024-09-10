import json
import os

# File to store transaction data
DATA_FILE = 'finance_tracker_data.json'

# Initialize data structures
data = {
    'income': 0.0,
    'expenses': 0.0,
    'savings': 0.0,
    'transactions': []
}

# Load data from file if it exists
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return data

# Save data to file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Print a welcome message
def print_welcome_message():
    print("Welcome to the Personal Finance Tracker!")
    print("Instructions:")
    print("1. Add income")
    print("2. Add expense")
    print("3. Generate report")
    print("4. Exit")

# Add income
def add_income(amount, description):
    data['income'] += amount
    data['transactions'].append({'type': 'income', 'amount': amount, 'description': description})
    save_data()

# Add expense
def add_expense(amount, description):
    data['expenses'] += amount
    data['transactions'].append({'type': 'expense', 'amount': amount, 'description': description})
    save_data()

# Calculate savings
def calculate_savings():
    data['savings'] = data['income'] - data['expenses']
    save_data()

# Generate a report
def generate_report():
    print("\n--- Financial Report ---")
    print(f"Total Income: ${data['income']:.2f}")
    print(f"Total Expenses: ${data['expenses']:.2f}")
    print(f"Total Savings: ${data['savings']:.2f}")
    print("\nTransactions:")
    for transaction in data['transactions']:
        print(f"{transaction['type'].capitalize()}: ${transaction['amount']:.2f} - {transaction['description']}")
    print("\n")

# Main function
def main():
    global data
    data = load_data()
    print_welcome_message()

    while True:
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            add_income(amount, description)
            calculate_savings()

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            add_expense(amount, description)
            calculate_savings()

        elif choice == '3':
            generate_report()

        elif choice == '4':
            print("Thank you for using the Personal Finance Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
