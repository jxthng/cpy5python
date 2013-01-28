# Filename: q5_upper_to_lower.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to converts an uppercase letter
# to a lowercase letter by making use of its ASCII value

# main

# Converts uppercase letters to lowercase letters

a = input ("Enter alphabet: ")

b = ord (a)

c = int (b)

d = (c + 32)

e = chr (d)

print ("Answer: " + str (e))


