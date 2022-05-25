#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large S
# Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1


print("Welcome to Burnside Pizza Delivery")
size = input("What size pizza would you like? S, M or L:\n ")
add_pepp = input("Would you like to add pepperoni? Y or N:\n ")
extra_cheese = input("Would you like extra cheese? Y or N:\n ")

price = 0

if size.casefold () == "S".casefold ():
    price += 15

elif size.casefold () == "M".casefold ():
    price += 20

else: 
    price += 25

if add_pepp.casefold () == "Y".casefold ():
    if size.casefold () == "S".casefold ():
        price += 2
    else: 
        price += 3

if extra_cheese.casefold () == "Y".casefold ():
    price += 1

print (f"Your final price is £{price}")


