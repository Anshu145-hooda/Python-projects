import random
import emoji
k = emoji.emojize(":rock:")
l = emoji.emojize(":page_facing_up:")
m = emoji.emojize(":scissors:")
print(f"Welecome to {k }  {l}  {m}")
set = ["stone" , "paper" , "scissors"]


def match():
   enter = input("enter your choice (stone/paper/scissors): ").lower()
   computer  = random.choice(set)
   if enter == computer:
       print(f"Its a draw \n your choice {enter} \n computer choice {computer}")
   elif(enter == "stone" and computer == "scissors" )  or\
        (enter == "paper" and computer == "stone") or \
        (enter == "scissors" and computer == "paper"):
        print(f"You win \n your choice {enter} \n computer choice {computer}" ) 
   elif enter in set:
        print("You lose!")
   else:
       print("no valid input")

def conti():
    while True:
      match()
      again = input(f"Do you wanna continue {k} {l} {m} ").lower()
      if again != "yes":
          print("GAME OVER")
          break
conti()
