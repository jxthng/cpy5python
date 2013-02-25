# Filename: q2_display_pattern.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to display a pattern

# main

# define display pattern

def display_pattern(n):
    prev_num = []
    for i in range(1, n + 1):
        prev_num.insert(0, str(i) + " ")
    length = len("".join(prev_num))
    prev_num = []

    for j in range(1,n+1):
        prev_num.insert(0, str(j) + " ")
        print("{0:>s}".format(("".join(prev_num))).rjust(length))


x = int(input("Enter an integer: "))

display_pattern(x)




