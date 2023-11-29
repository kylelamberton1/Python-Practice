#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
combi = [letters, numbers, symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password = ""

#for l in range(1,nr_letters + 1):
#  random_l = random.choice(letters)
#  password += random_l
#print (password)
  
#for s in range(1, nr_symbols + 1):
#  random_s = random.choice(symbols)
#  password += random_s
#print (password)
  
#for n in range(1, nr_numbers + 1):
#  random_n = random.choice(numbers)
#  password += random_n
#print (password)
#random = random.shuffle(password)
#print (random)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for l in range(1,nr_letters + 1):
  password_list.append(random.choice(letters))

for s in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for n in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))
  random.shuffle(password_list)

password = ""
for r in password_list:
  password += r
print(f" Your password is: {password}")