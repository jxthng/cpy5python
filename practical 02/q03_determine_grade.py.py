# Filename: q03_determine_grade.py
# Author: Thng Jing Xiong
# Created: 20130206
# Modified: 20130206
# Description: Program to determine your grade

#main

grade = int(input("Enter Score: "))

if 70<=grade<=100:
        print("Your grade is A")

elif 59<grade<70:
        print("Your grade is B")
        
elif 54<grade<60:
        print("Your grade is C")
       
elif 49<grade<55:
        print("Your grade is D")

elif 44<grade<50:
        print("Your grade is E")

elif 34<grade<45:
        print("Your grade is S")
        
elif 0<=grade<35:
        print("Your grade is U")
      
else:
        print("Invalid score! Please enter a number between 1-100")


