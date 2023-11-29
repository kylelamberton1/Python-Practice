print ("Hello")
num_char = len("Hello")
print (num_char)

def my_function():
  print("Hello")
  print("Bye")

my_function()

def turn_around():
  turn_left()
  turn_left()
def turn_right():
  turn_left()
  turn_around()

def hurdle():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

#for step in range(6):
#    hurdle()


#number_of_hurdles = 6 
#while number_of_hurdles >0:
#    hurdle()
#    number_of_hurdles -= 1
#    print(number_of_hurdles)

#while at_goal() != True:


#while not at_goal():
#  hurdle()

def turn_around():
  turn_left()
  turn_left()
def turn_right():
  turn_left()
  turn_around()

def hurdle():
  turn_left()
  while wall_on_right():
      move()
  else:
      turn_right()
      move()
      turn_right()
      move()
      while front_is_clear():
          move()
      else:
          turn_left()
#    HER DEF (SHORTER CODE)
#def hurdle():
  #turn_left()
  #while wall_on_right():
      #move()
  #turn_right()
  #move()
  #while front_is_clear():
      #move()
  #turn_left()


while not at_goal():
  if wall_in_front():
      jump()
  else:   
      move()
