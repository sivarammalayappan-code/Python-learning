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

#Number manipulation and f-string in python

print(22/7)   # Prints 3.142857142857143
print(round(22/7)) # Prints 3
print(round((22/7),2)) #Prints 3.14




