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