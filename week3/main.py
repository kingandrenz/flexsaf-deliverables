from validators import is_adult, is_authenticated

database = [{"username":"flexsaf","password": "flexsaf2026"},
        {"username":"Anthony", "password":"flexteck"}
        ]

def main():
    user_in = input("Username: ")
    pass_in = input("Password: ")

    if not is_authenticated(user_in, pass_in, database):
        print("Access Denied.")
        return
    else:
        print('\n---Successfully Logged in--')

    age = int(input("\nAge: "))
    if not is_adult(age):
        print("You are too young for these financial tools.")
        return

    print("\n1. Loan Checker\n2. Expense Tracker")
    choice = input("Select app: ")
    
    
    if choice == "1":
        import loan_app # Lazy loading
        loan_app.run_loan_checker()
    elif choice == "2":
        import finance
        user_income = int(input("\nPlease Enter Your Income: ")) 
        finance.expense_tracker(user_income)



if __name__ == "__main__":
    main()
