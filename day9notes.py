programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",       "Function": "A piece of code that you can easily call over and over again.",
}
#retrieving items from dictionary
print(programming_dictionary["Bug"])

#adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print (programming_dictionary)

#create new dictionary
empty_dictionary = {}

#wipe existing dictionary
#programming_dictionary = {}
#print (programming_dictionary)

#edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print (programming_dictionary)
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#nesting a list in a dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#nesting a dictionary in a dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 6},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 8},
}
#nesting a dictionary in a list
travel_log = [
  {"Country": "France",
   "cities_visited": ["Paris", "Lille", "Dijon"], 
   "total_visits": 6
  },
  {"Country": "Germany", 
   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
   "total_visits": 8
  },
]

