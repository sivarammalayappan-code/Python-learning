#----Printing----

#Include text inside "" to make it as string else it will error

print("Lets learn python!")



#-----String manipulation-----

# \n  will be used to print in new line

print("Hi There,\nHope you are doing good!")

# Concatenate strings

print("Hello"+"sivaram")       # It will print as Hellosivaram  . No space will be added
print("Hello"+" "+"sivaram")   # It will print as Hello sivaram . Now we can see space
print("Hello","sivaram")       # It will print as Hello sivaram . Now we can see space

#Inputs

#Using input function we can get inputs from user

input("Hi , How are you? : ")   #Once executed it will wait for user input

print("Hello" + input("What is your name? :")+"!") #No spaces will be added between each
print("Hello" , input("What is your name? :"),"!")  #Using comma will give space between each

#Variables

#Variables will hold the values and used in future
#If same variable name used twice it will only hold the last value

name= input("What is your name? : ")
print(name)

#Length function   len()

name= input("What is your name? : ")
print(len(name))

#Variable naming
#Always give a reasonable name to a variable so that you can able to understand after sometime
#Do not use the reserved words
#Do not use space in the variable name

# username="sivaram" -->good
# user_name="sivaram" -->good
# user name="sivaram" --> Not acceptable


#Project 1
#Band name generator

print("Welcome to the Band name Generator")
city=input("What's the name of the city you grew up in ? : \n")
pet_name=input("What's your pet's name : \n")
print("Your band name could be",city,pet_name)


#################################################################
#Datatype

#Check datatype

print(type("sivaram"))  # STRING
print(type(8893))       # INTEGER
print(type(8.88))       # FLOAT
print(type(None))       # None type
print(type(True))       # Boolean (True/False)

complex=3+4j
print(type(complex))    # complex (python uses j only)

#Apart from these set datatypes( set /frozenset)  , sequence datatype(list/tuple/range),
# mapping datatype (dict) , binary datatype (bytes,bytearray,memoryview)
#We will see it later

#Subscripting

#Always count from 0,1,2 ...

print("sivaram"[0])  #Prints only letter s
print("sivaram"[6])  #Prints only letter m
print("sivaram"[-1]) #Prints only letter m
print("sivaram"[-7]) #Prints only letter s

print("123" + "456") #Prints 123456 it will consider it as a string
print(123+456)       #Prints the added value 579 , it now consider it as string
print(1+0.5)         #Prints 1.5
print(1_2_3+4)       #Underscore will be hided by system . It will give 123+4=127. It can be used for large integers.

print(True)          #Prints True
print(False)         #Prints False

#Functions
#Each functions will work with particular datatype

#Length function

len("abc")    #Only take this datatype (string,list,tuple,range)


#Convert the datatypes using following functions

#int()
#float()
#str()
#bool()

print("111"+"111")              #Prints 111111
print(int("111")+int("111"))    #Prints the value 222

#Exercise
print("Number of letters in your name: " + str(len(input("Enter your name: "))))


#Mathematical operators
# addition +  , subtraction - , multiplying * , division /
#Even when we use / it will give result in float datatype only . Its default behaviour
#If we use // for division it will remove the float values and gives only integer but is not correct when we do something like diving 5 with 3.

print(1+2)    # Prints 3
print(2-1)    # Prints 1
print(3*2)    # Prints 6
print(4/2)    # Prints 2.0
print(4//2)   # Prints 2  . Removes the float
print(5//2)   # Prints 2  . Removes the float but  we will get wrong results. Value should be 2.5.

#Below is exponential operator give power of.
print(2**3)   # Prints 8 .  2*2*2  2 to the power of 2.

#Below is to take square root of numbers
import math
print(math.sqrt(4))             # Prints 2.0
print(int(math.sqrt(4)))        # Prints 2

#PEMDAS

#Paranthesis/Exponents/Multiplication/Division/Addintion/Subtraction

print(2*3/4+5-2**2+(2+2))  #Prints 6.5


#########################################################
#PROJECT 2
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
print("Dear",name,"your bmi is",bmi)

########################################################################################

#Number manipulation and f-string in python

print(22/7)                 # Prints 3.142857142857143
print(round(22/7))          # Prints 3
print(round((22/7),2))      #Prints 3.14

#To use a old variable value we can use as below

variable_1= 1
variable_1 = variable_1 + 1
print(variable_1)    # Prints 2.

#For the above scenario we can use like below .
variable_2= 1
variable_2 += 1
print(variable_2)  #Prints two . Same way we can use for other operations  -= , *= , /=


#f-string

name="siva"
age=32
weight=88.5

print("Dear",name,", \nyou are",age,"years old and your weight is",weight,"kg")

'''
Dear siva , 
you are 32 years old and your weight is 88.5 kg
'''

#Same output can be obtained with f-string easier

print(f"Dear {name} , \nyou are {age} years old and your weight is {weight} kg ")

###############################
project 3

#TIP CALCULATOR

print("Welcome to the tip calculator!")
bill=float(input("Enter the Bill amount : Rs "))
tip_percent=float(input("How much % you want to tip (10,12,15) : " ))
total_tip=(bill*tip_percent/100)
total_bill=bill+total_tip
print(f"Your total bill is {total_bill:.2f}")                              #.2f rounds the decimal to two place
no_of_person=int(input("How many people to share the bill : "))
final_amount=total_bill/no_of_person
print(f"Each person should pay {final_amount:.2f}")