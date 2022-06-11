import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

side = random.randint (0,1)
if side == 1: 
    print ("Heads")

else:
    print ("Tails") 
