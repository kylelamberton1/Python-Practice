#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
#list = [item for item in range(1, 101)] DIDNT NEED TO USE A LIST BIT STILL WORKED
number = randint(1,100)
print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")
print(f"FOR TESTING (number is {number})")
difficulty = input("choose a difficulty. Type 'easy' or 'hard': ").lower()

def easy():
  no_of_guess = 10
  while no_of_guess > 0:
    life = True
    print(f"You have {no_of_guess} attempts remaining to guess the correct answer")
    guess=int(input("make a guess: "))
    if guess < number:
      no_of_guess -= 1
      print("Too low")
    elif guess > number:
      no_of_guess -= 1
      print("Too high")
    else:
      print(f"You got it! The answer is {number}! ")
      break
  if no_of_guess == 0:  
    life == False
    print("You have run out of guesses. Game over!")

def hard():
  no_of_guess = 5
  while no_of_guess > 0:
    life = True
    print(f"You have {no_of_guess} attempts remaining to guess the correct answer")
    guess=int(input("make a guess: "))
    if guess < number:
      no_of_guess -= 1
      print("Too low")
    elif guess > number:
      no_of_guess -= 1
      print("Too high")
    else:
      print(f"You got it! The answer is {number}! ")
      break
  if no_of_guess == 0:  
    life == False
    print("You have run out of guesses. Game over!")

if difficulty == "easy":
  easy()
if difficulty == "hard":
  hard()

