# List of student grades (example: grades for each student)
students_grades = {
    'John': [85, 90, 78],
    'Alice': [92, 88, 91],
    'Bob': [79, 82, 88],
    'Diana': [91, 94, 89]
}

# Function to calculate the average grade for each student
def calculate_average(grades):
    return sum(grades) / len(grades)

# Open the text file in write mode
with open("student_avg_grades.txt", "w") as file:
    for student, grades in students_grades.items():
        avg_grade = calculate_average(grades)
        # Write the student's name and average grade to the file
        file.write(f"{student}: {avg_grade:.2f}\n")

print("Average grades have been written to 'student_avg_grades.txt'.")
