student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

for student, score in student_scores.items():
    if score > 91 and score < 100:
        student_grades[student] = "Outstanding"
    elif score > 81 and score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 71 and score < 80:
        student_grades[student] = "Acceptable"
    elif score < 70:
        student_grades[student] = "Fail"
print(student_grades)

    