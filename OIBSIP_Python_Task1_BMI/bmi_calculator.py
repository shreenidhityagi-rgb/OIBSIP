# BMI Calculator
# Task 1 - Oasis Infobyte Python Internship
# Author: Shreenidhi Tyagi

print("Welcome to the BMI Calculator")

weight = float(input("Please enter your weight (kg): "))
height = float(input("Please enter your height (m): "))

bmi = weight / (height ** 2)

print(f"Your calculated BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("BMI Category:", category)
print("Thank you for using the program!")
