#!/usr/bin/bash

def analyze_spending(income, expenses):
    """ Calculate what percentage of income is being spent"""
    spending_ratio = (expenses / income)
    percentage = spending_ratio * 100

    print(f"\n--- Spending Analysis ---")
    print(f"You are spending {percentage:.1f}% of your income.")

    if spending_ratio > 0.50:
        print("⚠️ ALERT: Overspending! Your expenses exceed 50% of your income.")
        print("Suggestion: Reduce discretionary spending before applying for a loan.")
    elif spending_ratio > 0.30:
        print(" WARNING: You are approaching a high debt-to-income ratio.")
    else:
        print(" Healthy: Your spending is well-managed.")


def expense_tracker(user_income):
    """ calls the analyze_spending helper function and checks if user has over spent based on incme"""
    try:
        total_exp = float(input("Enter your total expenses for this month: "))
        analyze_spending(user_income, total_exp)
    except ValueError:
        print("Please enter numeric values.")

