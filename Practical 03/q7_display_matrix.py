# Filename: q7_display_matrix.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to display a 'n' by 'n' matrix

# main

# import random

import random

# define matrix

def print_matrix(n):
    for i in range(0, n):
        for x in range (0, n):
            print(random.randint(0,1), end=" ")
        print(" ")

x = int(input("Enter an integer: "))

print_matrix(x)

