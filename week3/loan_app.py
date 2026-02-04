#!/usr/bin/python3


def run_loan_checker():
    """ check if a user is eligible to collect loan"""
    print("\n--- Loan Eligibility Checker ---")
    income = float(input("Enter monthly income: "))
    expenses = float(input("Enter monthly expenses: "))

    # I will be using 40% Debt-to-Income Rule
    limit = income * 0.40

    if expenses <= limit:
        print(f"Eligible! Your expenses are below the 40% limit (${limit:.2f}).")
    else:
        print(f"You are Ineligible for the loan. Your debt-to-income ratio is too high.")
