# Filename: q8_convert_milliseconds.py
# Author: Thng Jing Xiong
# Created: 20130221
# Description: Program to convert milliseconds to hours, minutes and seconds

# main

# Define conversion of milliseconds

def convert_ms(n):

    e = n / 1000

    a = int(e%60)

    b = int((e-a)/60)

    c = int(b%60)

    d = int((b-c)/60)

    print("Time in hours, minutes and seconds is " + str(d) +
          ":" + str(c) + ":" + str(a))

convert_ms(int(input("Enter time in milliseconds: ")))
