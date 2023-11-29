import random
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
game_images = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice >=3 or my_choice < 0:
    print ("you typed an invalid number. you lose")
else:    
    print (game_images[my_choice])

    comp_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[comp_choice])


    if my_choice == 0 and comp_choice == 2:
        print ("you win")
    elif comp_choice == 2 and my_choice == 0:
        print ("you lose")
    elif comp_choice > my_choice:
        print ("you lose")
    elif my_choice > comp_choice:
        print ("you win")
    elif comp_choice == my_choice:
        print ("it's a draw") 

