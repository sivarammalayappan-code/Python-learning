#TREASURE HUNT GAME

print("Welcome to the treasure Island!\nYour Mission is to find the TRESASURE!!!\nLets start the game")
way=input("Which way you want to go? : Type left or right : ").lower()

if way == "left":
    print("You chose the correct path! go ahead")
    cross_river=input("You have reached the river.\nDo you want to swim or wait? : ").lower()
    if cross_river == "wait":
        print("You chose the correct! A boat will pickup you in sometime!!\nFinally you arrived.\nChoose the door wisely!")
        door=input("Choose the door to open.  red / blue / yellow : ").lower()
        if door == "yellow":
            print("Congratulations!!!\nYou found the TREASURE!!!")
        elif door == "blue" or door == "red" :
            print("You chosed the wrong door. Game over!")
        else:
            print("Invalid input. Game over!")
    elif cross_river == "swim":
        print("Oh oh wrong decision. Crocs in river will eat you . Game over!!")
    else:
        print("Invalid input. Game over!")
elif way == "right":
    print("You have chosen wrong path!! Game over!!")
else:
    print("Invalid input. Game over!")