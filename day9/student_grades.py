student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

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

    