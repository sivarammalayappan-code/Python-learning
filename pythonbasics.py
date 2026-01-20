#VERY BASIC

#LEARNING FROM W3SCHOOL WEBSITE

#TAKING IMPORTANT HINTS TO REMEMBER

#--------  PRINT  ------#
#BOTH "" AND '' WE CAN USE

print("siva")
print('siva')

##########################################################################

#------- VARIABLE -----------#
'''
1. Variable case sensitive  a=1 and A=1 both are different
2. Variable can only use A to z / 0 to 9 / _
3. Variable can only start with letter or _ .  Should not start with number

Valid variables
---------------
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''
##Below is called casting.
##If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

##Multi Words Variable Names
'''
#CAMEL CASE
myVariableName = "John"
#Pascal Case
MyVariableName = "John"
#SNAKE CASE
my_variable_name = "John"

'''

##ASSIGN MULTIPLE VARIABLES IN SINGLE LINE

X,Y,Z="SIVA","RAM","M"
print(X,Y,Z) #Prints SIVA RAM M
print(X)     #Prints SIVA
print(Y)     #Prints RAM

##ONE VALUE TO MULTIPLE VARIABLES

D=E=F="SIVA"
#All below print will prints SIVA
print(D)
print(E)
print(F)

##UNPACK A COLLECTION

fruits = ["BANANA","GUAVA","JACKFRUIT"]

x,y,z = fruits

print(fruits)     #prints ['BANANA', 'GUAVA', 'JACKFRUIT']
print(fruits[0])  #prints BANANA
print(fruits[1])  #prints GUAVA
print(fruits[2])  #prints JACKFRUIT

print(x)          #prints BANANA
print(y)          #prints GUAVA
print(z)          #prints JACKFRUIT

##GLOBAL VARIABLES

#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()            #prints Python is awesome

##LOCAL VARIABLE
#If you create a variable with the same name inside a function, this variable will be local,
#and can only be used inside the function. The global variable with the same name will
# remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)  #prints Python is fantastic

myfunc()

print("Python is " + x)   #prints Python is awesome

##GLOBAL KEYWORD
#Normally, when you create a variable inside a function,
# that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x) #prints Python is fantastic

myfunc()

print("Python is " + x)   #prints Python is fantastic

#To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

x = "awesome"
print("Python is " + x)  #Python is awesome

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)  #Python is fantastic

myfunc()

print("Python is " + x)   #Python is fantastic


##
'''
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type           :	str
Numeric Types       :	int, float, complex
Sequence Types      :	list, tuple, range
Mapping Type        :	dict
Set Types           :	set, frozenset
Boolean Type        :	bool
Binary Types        :	bytes, bytearray, memoryview
None Type           :	NoneType

'''