student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
    student_grades = student_scores
    if student_grades[score] <= 70:
        student_grades[score] = "Fail"
    elif student_grades[score] > 70 and student_grades[score] <= 80:
        student_grades[score] = "Acceptable"
    elif student_grades[score] > 80 and student_grades[score] <= 90:
        student_grades[score] = "Exceeds Expectations"
    else:
        student_grades[score] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)