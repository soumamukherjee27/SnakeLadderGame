'''Snake Water Gun Project'''

import random

system = random.choice([0, 1 , 2])
youstr = input("Enter your choice: ")
youDict = {"s":0, "w":1, "g": 2}
reversedDict = {2: "Gun", 1: "Water", 0: "Snake"}

you = youDict[youstr] # Created 2 variables System & You

print(f"You chose {reversedDict[you]}\n System chose {reversedDict[system]}")

if (system == you):
    print("Its a Draw!")
else:
    if (system == 0 and you == 1):
        print("Opps! System Won! Snake ate all the Water")
    elif (system == 1 and you == 2):
        print("Opps! System Won! Guns don't work in Water")
    elif (system == 2 and you == 0):
        print("Opps! System Won! Snake killed by a gunshot")
    elif (system == 1  and you == 0):
        print("Hurray! You Won! Snake ate all the Water")
    elif (system == 2 and you == 1):
        print("Hurray! You Won! Guns don't work in Water")
    elif (system == 0 and you == 2):
        print("Hurray! You Won! Snake killed by a gunshot")
    else:
        ("Some Error Happened!") 

 