# Filename: q10_find_largest.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to find the largest n such that n3 < 12000

# main

a=1
while True:
    if a*a*a>12000:
        print (a-1)
        break
    a=a+1
