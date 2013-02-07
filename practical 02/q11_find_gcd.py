# Filename: q11_find_gcd.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to compute the greatest common divisor

# main

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
factor=1
a=2
while a<=num1 and a<=num2:
    if num1%a==0 and num2%a==0:
        factor=a
    a=a+1
print ("The grestest common divisor is " + format(factor))
