# Filename: q1_display_reverse.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to display an integer in reverse order

# main

# Display reverse

def reverse_int(n):
    return(int(str(n)[::-1]))


x = int(input("Enter Number: "))

print("The reversed integer is: " + str(reverse_int(x)))
