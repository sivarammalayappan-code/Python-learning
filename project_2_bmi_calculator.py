#BMI CALCULATOR

#BMI FORMULA
'''
BMI=Weight in kg/ Height in m²
'''

print("Welcome \nFind your BMI!!!")
name=input("Please enter your name : ")
weight=float(input("Please enter your weight(kg) : "))
height=float(input("Please enter your height(meter) : "))
bmi=(weight/height**2)
print("Dear",name,"your bmi is",round(bmi,2))