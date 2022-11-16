# import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)

# flip = random.randint(1, 2)

# if flip == 1:
#     print("Heads")
# else:
#     print("Tails")

states_of_ameirca = ['florida', 'delaware', 'pens']

states_of_ameirca.append('potato')

print(states_of_ameirca)

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97],
                           ["architecture", 65]]

# Your code below:

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85],
             ['history', 88]]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = [last_semester_gradebook] + [gradebook]
print(full_gradebook)
