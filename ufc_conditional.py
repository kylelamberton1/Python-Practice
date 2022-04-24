weight = int (input("Enter your weight big man! [KG]: \n"))

if weight >= 120:
    print("Heavyweight")
elif weight < 120 or weight >= 93:
    print("Light Heavyweight")
elif weight < 93 or weight >= 77:
    print("Middleweight")
elif weight < 77 or weight >= 70:
    print("Welterweight")
elif weight < 70 or weight >= 65:
    print("Lightweight")
elif weight < 65 or weight >= 61:
    print("Featherweight")
elif weight < 61 or weight >= 56:
    print("Bantamweight")
else: 
    print("Flyweight")    