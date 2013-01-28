# Filename: compute_bmi.py
# Author: Thng Jing Xiong 
# Created: 20130121
# Modified: 20130121
# Description: Program to get user weight and height and
# calculate body mass index (BMI)

# main

# prompt and get weight
weight = int(input("Enter weight in kg:"))

# prompt and get height
height = float(input("Enter height in m:"))

# calculate bmi
bmi = weight / (height * height)

# display result
print ("BMI={0:.2f}".format(bmi))

# determine health risk
if bmi >=27.50:
    print("High Risk!!!")
elif 23.5 <= bmi <27.5:
    print ("Moderate risk!!")
elif 18.5 <= bmi <23:
    print ("Healthy! :D")
else:
    print ("Malnutrition :(")
    
