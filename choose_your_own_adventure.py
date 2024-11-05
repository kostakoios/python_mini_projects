name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk arount it or swim acrross! Type walk or swim: ")
    if answer == "swim":
        print("You swam acrross and were eaten by an aligator.")
    elif answer == "walk":
        print("You walked a lot of miles without water and you lose!")
    else:
        print("Not a valid option you lose!")        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back. Type back or cross. ")
    if answer == "cross":
        print("You chose the right way, you won!")
    elif answer == "back":
        print("You go back and lose!") 
    else:
        print("Not a valid option you lose!")        
else:
    print("Not a valid version you lose!")