# Program to roll a dice and generate a random value 

import random
 
x = "y"
print("\nRolling the die...\n")

while x == "y":
     
    #Range = [1,6]

    z = random.randint(1,6)
     
    if z == 1:
        print("Output: 1")
        print("\n🟥")
    if z == 2:
        print("Output: 2")
        print("\n🟩 🟩")
    if z == 3:
        print("Output: 3")
        print("\n🟪 🟪 🟪")
    if z == 4:
        print("Output: 4")
        print("\n🟨 🟨\n\n🟨 🟨")
    if z == 5:
        print("Output: 5")
        print("\n🟦  🟦\n  🟦 \n🟦  🟦")
    if z == 6:
        print("Output: 6")
        print("\n⬜  ⬜\n\n⬜  ⬜\n\n⬜  ⬜")
         
    x=str(input("\nPress 'y' to roll again or press 'n' to exit: "))
    print("\n")

#End of the program