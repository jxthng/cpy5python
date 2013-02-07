# Filename: q06_kilograms_to_pounds.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to show kilograms and pounds

# main

a = 1
print("{0:<10} {1:>10}".format("Kilogram","Pounds"))
while (a<=10):
    print("{0:<10} {1:>10.1f}".format(str(a),float(int(a)*2.2)))
    a = a + 1


