
height = float(input("Enter your height in meters \n"))
weight = int(input("Enter your weight in kg \n"))
BMI = round(weight / height ** 2)
if BMI < 16:
    print(f"Your BMI is {BMI} - You are a skeleton!")
elif BMI < 19:
    print(f"Your BMI is {BMI} - You are a bit too skinny!")
elif BMI <25:
    print(f"Your BMI is {BMI} - You are a healthy weight!")
elif BMI <32:
    print(f"Your BMI is {BMI} - You have become a bit of a porker!")
else:
    print(f"Your BMI is {BMI} - Who ate all the pies? You did you fat bastard!!")

