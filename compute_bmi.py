# Filename: compute_bmi.py
# Author: Thng Jing Xionght and height 
# Created: 20130121
# Modified: 20130121
# Description: Program to get user weight and height and
# calculate body mass index (BMI)

# main

# prompt and get weight
weight = int(input("Enter weight in kg:"))

# prompt amd get height
height = float(input("Enter height in m:"))

# calculate bmi
bmi = weight / (height * height)

# display result
print ("BMI={0:.2f}".format(bmi))
