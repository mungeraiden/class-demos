# Aiden Munger
# 1/21/2026
# Python Basics 1

import math, datetime, random as rn

#################################################
# Basic Print
print("Hello, World!")

"""
This is a multi-line comment
that spans several lines.
"""
#################################################
# Variables

x = 78
y = 10.5

x = "This is a string now"

print(x, type(x))


x = True
x = False

###############################################
# Operators

x = 5 // 2
print(x, type(x))

x = 5 % 2

print(x, type(x))

x = 3 ** 2

print(x, type(x))

###############################################
# Math Module

x = math.pow(3, 2)
print(x)

###############################################
# Printing and Decimal Formatting

x = 10.55678
print(f"This is a string {x}")

print(f"x = {x:.2f}")

print(f"x = {round(x, 2)}")

###############################################
# USER INPUT

# fav_num = int(input("What is your favorite number?"))

# print(type(fav_num))
# print(f"Your favorite number is {fav_num + 1}")


###############################################
# Conditionals

temp = 600
humidity = 100

if temp < 45:
    print("It's cold outside")
elif temp > 80:
    print("It's hot outside")
    if humidity > 90:
        print("It's also very humid")
else:
    print("It's nice outside")
    
###############################################
# Loops


for num in [1, 6, 7]:
    print(num)

for letter in "hello":
    print(letter)

# for i in range(10, -1, -1):
#     print(i, end = " ")

for i in range(2, 39, 2):
    print(i, end = ", ")
print(i + 2)

x = 0

while x < 5:
    print(x)
    x += 1

x = 0
while x != 38:
    x += 2
    print(x, end = ", ")
print(x + 2)


###############################################

