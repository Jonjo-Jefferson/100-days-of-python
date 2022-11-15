# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

student_scores = [78, 65, 89, 86, 55, 91, 14, 89]

highest = 0

for score in student_scores:
    if score > highest:
        highest = score

print(f"The highest score in the class is: {highest}")
