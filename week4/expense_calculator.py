"""
Expense Calculator
------------------
This script allows users to record their expenses interactively.
For each entry, the user provides:
    - Amount (numeric value)
    - Category (e.g., Food, Rent, etc.)
    - Note (optional description)

The program stores each expense as a dictionary in a list.
After the user finishes entering expenses (by typing 'exit'),
it prints a summary showing each expense and the total amount spent.
"""

expenses = []

while True:
    print("\n--- New Entry (type 'exit' to finish) ---")
    amount_input = input("Enter Amount: ")
    if amount_input.lower() == 'exit':
        break
    
    try:
        amount = float(amount_input)
        category = input("Category (Food, Rent, etc): ")
        note = input("Note: ")
        
        # Store as dictionary
        expenses.append({"amount": amount, "category": category, "note": note})
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Expense Summary
print("\n--- Expense Summary ---")
total = 0
for item in expenses:
    print(f"{item['category']}: ₦{item['amount']:.2f}  ({item['note']})")
    total += item['amount']

print(f"Total Spent: ₦{total:.2f}")

    