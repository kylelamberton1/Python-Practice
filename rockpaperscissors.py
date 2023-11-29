rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = input ("Try to beat the computer in a game of rock, paper, scissors. Please enter (R) for rock, (P) for paper and (S) for scissors.\n")
RPS = ["R", "P", "S"]
index = RPS.index(choice)
if index == 0:
  print (rock)
elif index == 1:
  print (paper)
elif index == 2:
  print (scissors)
else:
  print ("error - please capital letter")

game = [rock, paper, scissors]
pick= random.choice(game)
index2 = game.index(pick)

print (pick)

if index == 0 and index2 == 0:
  print("it's a tie, try again")
elif index == 1 and index2 == 1:
  print("it's a tie, try again")
elif index == 2 and index2 == 2:
  print("it's a tie, try again")
elif index == 0 and index2 == 1:
  print("you lose")
elif index == 0 and index2 == 2:
  print("you win")
elif index == 1 and index2 == 0:
  print("you win")
elif index == 1 and index2 == 2:
  print("you lose")
elif index == 2 and index2 == 0:
  print("you lose")
elif index == 2 and index2 == 1:
  print("you win")






  