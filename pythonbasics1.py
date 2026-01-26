# Aiden Munger
# 1/21/2026
# Python Basics 1

import math
import random
from datetime import *

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
# Break and Continue

while True:
    user_input = input("Enter a word (\"stop\" to exit): ")
    if user_input.lower() == "stop":
        break
    if user_input == "next":
        continue
        print(user_input)
print("Outside the loop")

###############################################
# Functions

def my_msg(msg):
    """
    prints out msg with the date and time appended to the front    
    """
    print(f"{datetime.now()}: {msg}")

my_msg("This is a test message.")
my_msg("This is another message.")
my_msg("This is yet another message.")

def double(x):
    return x * 2

x = int(input("Enter a number to double"))
print(double(x))

def circle(radius):
    return 2 * math.pi * radius, math.pi * radius ** 2

radius = float(input("Enter the radius of a circle: "))
circumference, area = circle(radius)
print(f"Circumference: {circumference:.2f}, Area: {area:.2f}")

###############################################
# Random

random.seed(0)   # sets the seed for reproducibility

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)
print(f"Rolls: {roll1}, {roll2}, {roll3}")


###############################################
# Lists

list_ints = [2, 100, 5, -10]

