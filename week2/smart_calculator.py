#!/usr/bin/python3


#accept input for test score, assignment score, and exam score
#perform arithmetic operation to calculate the total and average score
#use compairison  operation to check if the student pass or fail
#and logical if the student qualifies for and award


# ---- validation functions ----

def get_valid_score(prompt):
    """Ensures the user enters a number between 0 and 100."""
    while True:
        score_input = input(prompt).strip()
        if score_input.isdigit() and 0 <= int(score_input) <= 100:
            return int(score_input)
        print("Invalid input: Please enter a number between 0 and 100.")

# ---- implentation function ----

def grade_calc():
    """ accept student scores and calculate their grades,
        checks if they are eligible for an Award
    """

    print("--- Student Grade & Award Calculator ---")
    
    test = get_valid_score("Enter test score: ")
    assignment = get_valid_score("Enter assignment score: ")
    exam = get_valid_score("Enter exam score: ")

    total = test + assignment + exam
    # Using the formula: Average = Total / Number of Subjects
    average = total / 3

    # Pass threshold: 50 | Award threshold: Average > 90 AND Exam > 85
    passed = average >= 50
    qualifies_for_award = average > 90 and exam > 85

    print("\n" + "="*30)
    print(f"Total Score:   {total}")
    print(f"Average Score: {average:.2f}")
    print(f"Status:        {'PASS' if passed else 'FAIL'}")
    
    if qualifies_for_award:
        print("Congratulations! You qualify for the Academic Excellence Award!")
    elif passed:
        print("Well done on passing.")
    else:
        print("Keep studying! You'll get it next time.")
    print("="*30)

if __name__ == "__main__":
    grade_calc()


