# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hello")
  print("Hola")
  print("Konichiwa")

greet()

#Function that allows for input
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"Hola {name}")
  print(f"Konichiwa {name}")
  
greet_with_name("Kyle") 
#Functions with more than one input

def greet_with(name, location):
  print (f"Hello {name}")
  print (f"What is it like in {location}?")
greet_with("Kyle", "Valencia")
#Functions with keyword arguments
greet_with(name="Kyle", location="London")