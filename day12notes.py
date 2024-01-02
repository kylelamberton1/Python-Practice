################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # LOCAL SCOPE

# def drink_potion():
#   potion_strength = 2
#   print (potion_strength)
# drink_potion()
# print (potion_strength)

# GLOBAL SCOPE
# player_health = 10
# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#   drink_potion()

# THERE IS NO BLOCK SCOPE

# game_level = 3
# def create_enemy():
#   enemies = ["skeleton", "zombie", "alien"]
#   if game_level <5:
#     new_enemy = enemies[0]

#   print(new_enemy)

#### MODIFYING GLOBAL SCOPE
# enemies = "skeleton"
# def increase_enemies():
#   enemies = "zombie"
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

####GLOBAL CONSTANTS
### upper case
PI = 3.14159
URL = "http://www.google.com"
TWITTER_HANDLE = "@yu_angela"
def createList():
  return [item for item in range(1, 101)]





