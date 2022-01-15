print("What would you like today?")
print("                            Menu                       ")
print("1- Pizza      15$\n2- Burger     10$\n3- Tacos      20$\n4- Crepe      15$\n5- Fries      5$\n")
menu = {1: 15, 2: 10, 3: 20, 4: 15, 5: 5}
choice1 = int(input("Enter a number between 1 and 5:\n"))
if choice1 < 0 or choice1 > 5:
    print("Error, Please enter a number between 1 and 5!\n")
    exit()
choice2 = int(input("How many Would you like:\n"))
if choice2 < 0:
    print("Error, Please enter a positive number:\n")
    exit()
total = menu[choice1]*choice2
print("your total will be:")
print(total)