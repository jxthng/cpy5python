# Filename: q6_determine_prime.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to find first thousand prime numbers

# main

# import math

from math import *

# define prime

def is_prime(n):
    for a in range (2, int(sqrt(n) + 1)):
        if n % a == 0:
            return False
        return True
c = []

d = 2
while len(c) < 1000:
    b = is_prime(d)
    if b == True:
        c.append(d)
    d = d + 1    
k = 0
while k < 1000:
    print(c[k], c[k+1], c[k+2], c[k+3], c[k+4], c[k+5], c[k+6], c[k+7], c[k+8],
          c[k+9])
    k = k + 10

