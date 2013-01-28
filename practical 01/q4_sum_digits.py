# Filename: q4_sum_digits.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to add all digits in the integer

# main

# To add all digits in the integer

a = input("Enter Number:")

b = int (a)

c = b % 10

d = ((b % 100) - c) // 10

e = ( b - ( b % 100 )) // 100

f = c + d + e

print ("The sum of all digits in the integer is: " + str(f) )
