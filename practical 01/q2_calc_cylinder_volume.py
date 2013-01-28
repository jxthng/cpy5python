# Filename: q2_calc_cylinder_volume.py
# Author: Thng Jing Xiong
# Created: 20130122
# Modified: 20130122
# Description: Program to calculate volume of cylinder

#main

#calculate cylinder volume
a = input ("Enter unit of measurement:")

b = input ("Enter height of cylinder:")

height = float (b)

c = input ("Enter radius of cylinder:")

radius = float (c)

import math

d = "{0:<.3f}".format(float ( math.pi * radius * radius * height ))

print ("The volume is: " + str (d) + " " + str (a) + chr (0x00B3))


