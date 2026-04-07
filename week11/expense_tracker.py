import csv
import pandas as pd
from datetime import datetime

FILE_NAME = "expenses.csv"


def log_expense(description, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        # write header if file is empty
        if file.tell() == 0:
            writer.writerow(["timestamp", "description", "amount"])

        writer.writerow([timestamp, description, amount])

    print("Expense saved successfully.")


def show_summary():
    try:
        df = pd.read_csv(FILE_NAME)

        total_spent = df["amount"].sum()
        avg_expense = df["amount"].mean()

        print("\nExpense Summary")
        print("------------------")
        print("Total Spent:", total_spent)
        print("Average Expense:", avg_expense)

    except FileNotFoundError:
        print("No expenses recorded yet.")


def main():
    while True:
        print("\n1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            description = input("Expense description: ")
            amount = float(input("Amount: "))
            log_expense(description, amount)

        elif choice == "2":
            show_summary()

        elif choice == "3":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
