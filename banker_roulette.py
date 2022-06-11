import random



# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people = (len(names))
random_no = random.randint (0, people - 1)
person = names [random_no]

print (f"{person} is going to buy the meal today")


#easy way but not the challenge
#person = random.choice(names)
#print(person + " is going to buy the meal today!")

