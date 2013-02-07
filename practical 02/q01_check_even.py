# Filename: q01_check_even.py
# Author: Thng Jing Xiong
# Created: 20130129
# Modified: 20130129
# Description: Program to check if an integer is odd or even

# main

# Prompt and get number
number = int(input("Enter Number: "))

# Check if number is even
if number % 2 == 1:
    print (format(number) + " is odd")

else:
    print (format(number) + " is even")
