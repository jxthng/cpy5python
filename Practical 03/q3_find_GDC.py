# Filename: q3_find_gcd.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to find GCD between two positive integers

# main

# Define GCD

def gcd(m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    return gcd(n, (m % n))

# GCD of (24, 16) and (255, 25)

print(gcd(24, 16))

print(gcd(255, 25))
