# Filename: q1_fahrenheit_to_celsius.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to convert fahrenheit to celsius

# main

# prompt originial unit
print ("celsius or fahrenheit")

a = input ("Original Unit:")

c = input ("Value:")

d = float (c)

# Conversion
if a == "celsius":
    z = "°F"
if a == "fahrenheit":
    z = "°C"
if a == "celsius":
    e = "{0:<.1f}".format (float(d * 9 / 5 + 32))
elif a == "fahrenheit":
    e = "{0:<.1f}".format(float((d - 32) / 9 * 5))
print ("Your answer is: " + str(e) + str(z))
