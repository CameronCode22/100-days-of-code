student_scores = [125, 344, 166, 97]

print(max(student_scores))


stored = 0
for score in student_scores:
    if score > stored:
        stored = score

print(stored)