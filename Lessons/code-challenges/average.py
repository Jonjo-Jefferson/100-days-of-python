# complete without using sum() or len()

student_heights = [180, 124, 165, 173, 189, 169, 146]

total_number = 0
add_heights = 0

for count in student_heights:
    total_number += 1

for student in student_heights:
    add_heights = add_heights + student

average = add_heights / total_number

print(round(average))
