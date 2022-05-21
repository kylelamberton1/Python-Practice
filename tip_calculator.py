

print("Welcome to the tip calculator")
bill = float(input("what was the total price?\n"))
people = int(input("How many people are dining?\n"))
tip = int(input("What percentage tip would you like to pay? 10, 12 or 15?\n"))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount 
split = total_bill / people
total_split = round(split, 2) 
total_split = "{:.2f}".format(split) 
print(f"The amount to pay is £{total_split} per person")