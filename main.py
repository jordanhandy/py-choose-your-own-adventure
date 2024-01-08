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

step1 = input("You are at a crossroads.  Do you turn left or right?  Type 'left' or 'right' to continue\n").lower()
if step1 == "left":
  step2 = input("You have come across a river.  Do you swim across it, or wait for a boat?  Type 'swim' or 'wait'\n").lower()
  if step2 == 'wait':
    step3 = input("You come across three doors. One red, one blue, and one yellow.  Which door do you enter?  Enter 'red' 'blue' or 'yellow' to make your choice\n").lower()
    if step3 == 'red':
      print("You were burned by fire.  GAME OVER\n")
    elif step3 == 'blue':
      print("You were eaten by beasts. GAME OVER\n")
    elif step3 == 'yellow':
      print("Congratulations.  You win the game!!\n")
    else:
      print("You could not follow simple instructions.  GAME OVER\n")  
  else:
    print('You were attacked by deadly trout and drowned.  GAME OVER\n')
else:
  print('You have fallen into a hole. GAME OVER\n')
