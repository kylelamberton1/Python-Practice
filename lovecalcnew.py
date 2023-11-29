print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both_names = name1.lower() + name2.lower()
T = both_names.count("t") 
R = both_names.count("r")
U = both_names.count("u")
E = both_names.count("e")
true = str(T + R + U + E)
L = both_names.count("l")
O = both_names.count("o")
V = both_names.count("v")
E = both_names.count("e")
love = str(L + O + V + E)
truelove = int(true + love)
if truelove <= 10 or truelove>= 90:
  print (f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove <= 50 and truelove >= 40:
  print (f"Your score is {truelove}, you are alright together.")
else:
  print (f"Your score is {truelove}.")

