print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

forest = input('You arrive at an intersection in a forest. You can go left or right. Type "left" or "right".').lower()
print()
if forest == "left":
        dock = input('You made it to an opening with a lake that has an island in the middle. You can choose to "wait" for a boat to land at the dock or "swim" yourself. Type "wait" or "swim".').lower()
        print()
        if dock == "wait":

            door = input('Patience paid off! A boat arrived and brought you to the island. A house with three doors await; blue, red or yellow. Type "red", "blue" or "yellow"?').lower()
            print()
            if door == "blue":
                print("The door opens and you are greeted by a ninja looking for the same treasure. GAME OVER.")
                exit()
            elif door == "yellow":
                print("As the door opens the glistening of treasure overwhelms your eyes. There is enough treasure to make Jack Sparrow blush. YOU WIN!")
                exit()
            else:
                   print("The door opens to what looks like treasure, however it is only a mural. An explosion is heard and suddenly the house collapses on itself. GAME OVER. ")
        else:
            print("A bull shark has mistaken you for lunch. GAME OVER.")
            exit()
else:
    print("You came upon a witches caves and were turned into a gnat. GAME OVER")
exit()
