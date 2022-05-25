print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride")
  age = int(input("what is your age? "))
  if age < 12:
    bill = 5
    print("child tickets are $5")
  elif age <= 18:
    bill = 7
    print("youth tickets are $7")
  else:
    bill = 12
    print("adult tickets are $12")

  wants_photo = input("photo? Y or N ")
  if wants_photo.casefold() == "Y".casefold():
    bill +=3
  print(f"Your final bill is ${bill}")

else:
    print("You can't ride")