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

