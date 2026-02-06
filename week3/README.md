# Financial Suite (Loan & Expense Tracker)

A modular Python application to manage user authentication, age validation, and financial health checks.

---

## 📂 Project Structure
- **main.py**: The entry point/menu system  
- **validators.py**: Handles login and age verification logic  
- **expense_tracker.py**: Analyzes spending relative to income  
- **loan_app.py**: Evaluates loan eligibility based on Debt-to-Income (DTI)  

---

## ✨ Features
- **Secure Gatekeeping**: Validates user credentials and age (≥ 18)  
- **Smart Tracking**: Flags overspending if expenses exceed 50% of income  
- **Loan Assessment**: Checks if the debt-to-income ratio is within the 40% threshold  

---

## ▶️ How to Run
1. **Prepare Files**: Ensure all `.py` files are in the same directory.  
2. **Execute**: Run the following command in your terminal:  
   ```bash
   python3 main.py
   ```

3. Credentials: Use default login:

### Username: flexsaf

### Password: flexsaf2026


## 🧮 Logic Overview

| App              | Threshold            | Alert Trigger                          |
|------------------|----------------------|----------------------------------------|
| Expense Tracker  | 50% of Income        | "Overspending" warning if exceeded     |
| Loan Checker     | 40% of Income (DTI)  | "Ineligible" if expenses are higher    |

