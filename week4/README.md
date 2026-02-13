# 📝 Project README

## Overview

This repository contains two simple Python scripts designed for everyday
utility:

1.  **Password Strength Checker** -- evaluates the strength of
    user-entered passwords based on length, character diversity, and
    symbol usage.\
2.  **Expense Calculator** -- allows users to log expenses interactively
    and view a summary of spending.

------------------------------------------------------------------------

## 📌 1. Password Strength Checker (`check_password.py`)

### Description

The script prompts the user to enter a password and evaluates its
strength by checking:

-   Minimum length (≥ 8 characters)\
-   Presence of uppercase letters\
-   Presence of lowercase letters\
-   Presence of digits\
-   Presence of special characters (`@!#$%^&*()-_=+[]{};:,.<>?`)

It returns: - A **score** (numeric)\
- A **label** (e.g., "Weak", "Strong")\
- **Tips** for improvement

### Example Usage

``` bash
$ python check_password.py
Please Enter Password: MyPass123!
(5, 'Very Strong', [])
```

------------------------------------------------------------------------

## 📌 2. Expense Calculator (`expense_calculator.py`)

### Description

This script helps users track expenses interactively. For each entry,
the user provides:

-   Amount (numeric value)\
-   Category (e.g., Food, Rent, Transport)\
-   Note (optional description)

Expenses are stored in a list of dictionaries. After the user finishes
(by typing `exit`), the program prints a summary of all expenses and the
total amount spent.

### Example Usage

``` bash
$ python expense_calculator.py

--- New Entry (type 'exit' to finish) ---
Enter Amount: 2500
Category (Food, Rent, etc): Food
Note: Lunch

--- New Entry (type 'exit' to finish) ---
Enter Amount: exit

--- Expense Summary ---
Food: ₦2500.00  (Lunch)
Total Spent: ₦2500.00
```

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x\
-   No external libraries required (uses only built-in functions)

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone or download this repository.\
2.  Run the scripts using:

``` bash
python check_password.py
python expense_calculator.py
```

------------------------------------------------------------------------

