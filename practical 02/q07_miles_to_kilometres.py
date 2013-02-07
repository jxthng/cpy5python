# Filename: q07_miles_to_kilometres.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to show miles and kilometres

# main

a = 1
b = 20
print("{0:<} {1:<} {2:<} {3:<}".format("Miles","Kilometre","Kilometre","miles"))
while ((a<=10) and (b<=65)):
    print("{0:<5} {1:<9.3f} {2:<9} {3:<.3f}".format(str(a),float(int(a)*1.609),
                                                   str(b),float(int(b)/1.609)))
    a = a + 1
    b = b + 5

