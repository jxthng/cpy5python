# Filename: q04_determine_leap_year.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to determine a leap year

# main

# Prompt and get year
a = int(input("Enter year: "))

if a%4!=0:
    print (format(a) + " is a non-leap year.")

else:
    if a%400==0:
        print (format(a) + " is a leap year.")
    else:
        if a%100==0:
            print (format(a) + " is a non-leap year.")
        else:
            print (format(a) + " is a leap year.")
