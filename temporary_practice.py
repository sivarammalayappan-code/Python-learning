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