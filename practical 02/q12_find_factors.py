# Filename: q12_find_factors.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to find the factors of an integer

# main

a = int(input("Enter number: "))
b = 2
while (a/b>=1):
    if(a%b==0):
        print(b)
        a=a/b
    else:
        b = b + 1
