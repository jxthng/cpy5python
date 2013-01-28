# Filename: q3_miles_to_kilometre.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to convert miles to kilometres

#main

#Converting miles to kilometres
print ("Converting Miles to Kilometres")

mile = 1.60934

a = input ("Number of miles:")

b = float (a)

c = "{0:<.3f}".format (float (b * mile))

print ("Number of kilometres:" + str(c) + "km")
