# Filename: q2_triangle.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to calculate the perimeter of a triangle

# main

# Prompt and get number
number = float(input("Enter side 1: "))
side = float(input("Enter side 2: "))
base = float(input("Enter side 3: "))

# Find Perimeter
Perimeter = number + side + base

# Check if perimeter is valid
if (number + side) <= base:
    print ("Invalid Triangle!")
elif (number + base) <= side:
    print ("Invalid Triangle!")
elif (base + side) <= number:
    print ("Invalid Triangle!")
else:
    print ("Perimeter = {0:.2f}".format(Perimeter))
