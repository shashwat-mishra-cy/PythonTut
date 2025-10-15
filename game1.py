import sys
import random
from enum import Enum

class RPS (Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3

print ("")
playerchoice=input("Press 1 for ROCK\nPress 2 for PAPER\nPress 3 for SCISSORS\n")
player=int(playerchoice)
if player<1 or player>3:
    sys.exit("Invalid Input")

print ("")
computerchoice=random.choice("123")
computer=int(computerchoice)

print("")
print("Your choice is "+ str(RPS(player)).split('.')[1])
print("Computer choice is "+ str(RPS(computer)).split('.')[1])

if player==1 and computer==3:
    print("You Win!")
elif player==2 and computer==1:
    print("You Win!")
elif player==3 and computer==2:
    print("You Win!")
elif player==computer:
    print("Tie Game!")
else:
    print("Computer Wins!")
