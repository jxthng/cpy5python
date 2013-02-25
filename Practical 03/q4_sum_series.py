# Filename: q4_sum_series.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to compute sum series

# main

# def sum series

def m_series(i):
    a = 0
    b = 1
    c = 2
    while b <= i:
        a = float (a + b / c)
        b = b + 1
        c = c + 1
    d = "{0:<.4f}".format (a)
    print (d)

running = True

while running:
    m_series(float(input("Enter Number: ")))
