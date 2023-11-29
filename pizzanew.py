print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill = 15
  
  if add_pepperoni == "Y":
    bill = 17
    
elif size == "M":
  bill = 20
  
  if add_pepperoni == "Y":
    bill = 23

elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = 28
else:
  print("There has been an error. Please try again.")
    
if extra_cheese == "Y":
  bill += 1
  print(f"Your final bill is: ${bill}.")
else:
  bill += 0
  print(f"Your final bill is: ${bill}.")