import random

# toppings = [
#     "pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies",
#     "mushrooms"
# ]

# prices = [2, 6, 1, 3, 2, 7, 2]

# num_two_dollar_slices = prices.count(2)

# num_pizzas = len(toppings)

# print(f"We sell {num_pizzas} different kinds of pizza!")

# pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"],
#                     [3, "sausage"], [2, "olives"], [7, "anchovies"],
#                     [2, "mushrooms"]]

# sorted = sorted(pizza_and_prices)

# cheapest_pizza = sorted[0]
# priciest_pizza = sorted[-1]

# random_words = ["apple", "pepperoni", "potato", "sausage"]
# i = random.randint(0, len(random_words) - 1)
# print(f"The random number is {i} - " + random_words[i])
# for word in random_words:
#     print(word)


chance_to_rain = [85, 80, 79, 94, 88]
print(sum(chance_to_rain))
for chance in chance_to_rain:
    average_rain = sum(chance_to_rain) / len(chance_to_rain)
print(round(average_rain))

# Method 1: using return value inside another function
def fun1(a):
    res = a + 1
    return res


def fun2(c):
    res = c * 2
    return res


output = fun1(fun2(1))
print(output)
# Method 2: directly calling one function in the other
def function_1(n):
    v = n * n
    num = function_2(v)
    return num


def function_2(a_number):
    a_number = a_number * 2
    return a_number


print(function_1(10))
