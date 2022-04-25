weight = float (input("Enter your weight big man! [KG]: \n"))

if weight < 56:
    print("Flyweight")
elif weight < 61:
    print("Bantamweight")
elif weight < 65:
    print("Featherweight")
elif weight < 70:
    print("Lightweight")
elif weight < 77:
    print("Welterweight")
elif weight < 93:
    print("Middleweight")
elif weight < 120:
    print("Light Heavyweight")
else: 
    print("Heavyweight \n")

input("KEEP PUNCHING CHAMP!")
    