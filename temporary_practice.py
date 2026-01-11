#Pizza order

print("Welcome to Pizza Hub !")
pizza_size=input("Enter the pizza size S for small, M for medium or L for large :  ").upper()
bill=0

if pizza_size =="S":
    bill=25
    pepperoni =input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni =="Y":
        bill += 5
    elif pepperoni =="N":
        bill= 25
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is {bill}")
    elif extra_cheese == "N":
        print(f"your bill is {bill}")
    else:
        print("Please enter correct value")

elif pizza_size == "M":
    bill = 50
    pepperoni = input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni == "Y":
        bill += 10
    elif pepperoni == "N":
        bill = 50
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is {bill}")
    elif extra_cheese == "N":
        print(f"your bill is {bill}")
    else:
        print("Please enter correct value")

elif pizza_size == "L":
    bill = 100
    pepperoni = input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni == "Y":
        bill += 10
    elif pepperoni == "N":
        bill = 100
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is {bill}")
    elif extra_cheese == "N":
        print(f"your bill is {bill}")
    else:
        print("Please enter correct value")

else:
    print("Please enter correct value")