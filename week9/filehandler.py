import csv

# Student data
students = [
        ["Name", "Score"],
        ["Nnenna", 85],
        ["Emeka", 92],
        ["Michael", 78],
        ["David", 88],
        ["Aminat", 95]
        ]

filename = "students.csv"

# Writing to CSV using context manager.
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)

    print("Student data successfully written to CSV.\n")

# Read CSV and process data.
total_score = 0
count = 0
top_score = -1
top_student = ""

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        score = int(row[1])

        total_score += score
        count += 1

        if score > top_score:
            top_score = score
            top_student = name
            
# Calculate average.
average = total_score / count  if count > 0 else 0

# Display result.
print(f"Class Average: {average:.2f}")
print(f"Top Performer: {top_student} with score {top_score}")
