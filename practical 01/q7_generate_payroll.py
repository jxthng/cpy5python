# Filename: q7_generate_payroll.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to calcualte the payroll

# main

# Generate Payroll

name = input("Enter name: ")

hours = input("Enter number of hours worked weekly: ")

rate = input("Enter hourly pay rate: ")

CPF = input("Enter CPF contribution rate(%): ")

h = float (hours)
r = float (rate)
gross = float (h * r)
c = float (CPF)
p = float (c / 100)
f = float (p * gross)
n = "{0:<.2f}".format (float (gross - f))

print (" ")
print (" ")
print ("Payroll statement for: " + str (name))
print ("Number of hours worked in this week: " + str (hours))
print ("Hourly pay rate: " + str (rate))
print ("Gross pay: " + str (gross))
print ("CPF contribution at " + str (CPF) + "%: " + str (f))
print ("Net pay = $" + str(n))

