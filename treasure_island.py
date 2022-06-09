print ("Welcome to Egle's big Oxford street shopping trip!!!!")
print ("Your mission is to find a new dress. Good luck!")

transport = input ("You wake up nice and get out of the house before 8am. Do you take a train or uber?\n").lower()

if transport == ("uber"):
    money = int(input("The driver is a nutter but gets you to the city before 9am. How much cash do you draw out from the ATM?\n"))

    if money >= 50 and money < 200:
        colour = input ("You make it to Topshop and find the perfect dress. What colour do you choose?\n").lower()

        if colour == ("red"):
            print("You look like a prostitute. GAME OVER!")
        elif colour == ("blue"):
            print("It looks beautiful. WELL DONE!")
        elif colour == ("black"):
            print("You look like a goth. GAME OVER!")
        elif colour == ("green"):
            print("It looks beautiful. WELL DONE!")
        elif colour == ("white"):
            print("It looks beautiful. WELL DONE!")
        else:
            print("It looks awful. GAME OVER!")

    elif money >= 200:
        print("You get mugged in the street by a crackhead. GAME OVER!")
    else:
        print("You are a cheapskate and can't afford thre dress you like! GAME OVER!")

else:
    print("The shitty South Eastern Railway has signalling issues again! You arrive two hours late and miss all the nice dresses. GAME OVER!!!!")
    
