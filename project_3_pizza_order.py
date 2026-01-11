#Pizza order

print("Welcome to Python Pizza Deliveries!")
pizza_size=input("Enter the pizza size S for small, M for medium or L for large :  ").upper()
bill=0

if pizza_size =="S":
    bill=15
    pepperoni =input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni =="Y":
        bill += 3
    elif pepperoni =="N":
        bill= 15
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "N":
        print(f"Your final bill is: ${bill}.")
    else:
        print("Please enter correct value")

elif pizza_size == "M":
    bill = 20
    pepperoni = input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill = 20
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "N":
        print(f"Your final bill is: ${bill}.")
    else:
        print("Please enter correct value")

elif pizza_size == "L":
    bill = 25
    pepperoni = input("Do you want to add pepperoni? Type y for yes or n for no : ").upper()

    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill = 25
    else:
        print("Please enter correct value")

    extra_cheese = input("Do you want extra cheese ? Type y for yes or n for no : ").upper()
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "N":
        print(f"Your final bill is: ${bill}.")
    else:
        print("Please enter correct value")

else:
    print("Please enter correct value")