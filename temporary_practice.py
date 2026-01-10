#Conditional statements/ logical operators / code blocks / scope

#IF ELSE STATEMENT
'''
if condition:
    do this
else:
    do this
'''

#Logical operators

'''
< - less than
> - greater than
<= - less than or equal to
>= - greater than or equal to
== - equal to
!= - not equal to
'''
################################
#Roller coaster entrance check to allow only people above 120 cm height

print("Welcome to roller coaster ride!")
height=int((input("Enter your height in cm : ")))

if height >= 120 :
    print("Enjoy the ride sir!")
else:
    print("Sorry you are not allowed to ride")


#Modulo Operator  %
# It will return the reminder value

print(10%3)   # Prints the remainder value 1.
print(10%2)   # Prints the remainder value 2.

#Find odd or even

number=int(input("Enter a number to check: "))

if number%2 == 0:
    print("Its even number!")
else:
    print("Its odd number!")

#Nested statements
#if statement inside if statement

'''
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
'''
print("Welcome to Roller Coaster ride!")
height=int(input("Please enter your height in cm : "))
if height >= 120:
    age=int(input("Please enter your age : "))
    if age < 18:
        print("Your ticket price is Rs 50")
    else:
        print("Yout ticket price is Rs 100")
else:
    print("Sorry, You are not allowed for roller coaster ride.")

#Elif statement

'''
if condition1:
    do A
elif condition2:
    do B
else:
    do this
'''

print("Welcome to Roller Coaster ride!")
height = int(input("Please enter your height in cm : "))
if height >= 120:
    age = int(input("Please enter your age : "))
    if age < 18:
        print("Your ticket price is Rs 50")
    elif age >= 18 and age <=21:    #It can be written as   18 <= age <= 21
        print("Your ticket price is Rs 75")
    else:
        print("Yout ticket price is Rs 100")
else:
    print("Sorry, You are not allowed for roller coaster ride.")


#Multiple if statements

print("Welcome to Roller Coaster ride!")
height = int(input("Please enter your height in cm : "))
bill=0
if height >= 120:
    age = int(input("Please enter your age : "))
    if age < 18:
       bill=50
       print("Ticket price is Rs 50")
    elif age >= 18 and age <=21:    #It can be written as   18 <= age <= 21
        bill=75
        print("Ticket price is Rs 75")
    else:
        bill=100
        print("Ticket price is Rs 100")

    photo=input("Are you willing to take photo ? . Please type Y for yes OR N for no : ").upper()
    if photo == "N":
        print(f"Your total bill is {bill}")
    else:
        bill += 12
        print(f"Your total bill is {bill} ")
else:
    print("Sorry, You are not allowed for roller coaster ride.")
