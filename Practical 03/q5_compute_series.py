# Filename: q5_compute_series.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to compute a required series

# main

# Define (m)

def m(i):
    a = 0
    b = 0
    c = 1
    d = 3

    while c <= (2*i - 1):
        a = (1 / c) - (1 / d)
        b = b + a
        c = c + 4
        d = d + 4

    e = 4 * b
    print(e)

running = True

while running:
    m(float(input("Enter Number: ")))


    
