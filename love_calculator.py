print("Welcome to the love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

both_names = name1 + name2
lower_names = both_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
true = t+r+u+e
l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
love = l+o+v+e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your love score is {score} You go together like ice-cream and bacon!")

elif score < 50 and score > 40:
    print(f"Your love score is {score} You are perfect together!")

else:
    print(f"Your love score is {score} It could work out for you but don't get too excited!")
