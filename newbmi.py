#Data Types

# num_chara = len(input("what is your name?"))

# new_num_chara = str(num_chara)
# print("your name has " + new_num_chara + " characters.")   
#PEMDAS PARENTHESIS EXPONENTS MULT/DIV ADD/SUBT
#()
#**
#* /
#+ -
#print(2**3)
#print(3 * (3 + 3) / 3 - 3)
# 1st input: enter height in meters e.g: 1.65
height = input("What is your height?")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weightbmi = int(weight)
heightbmi = float(height)
bmi = (weightbmi) / (heightbmi) **2
bmireal = int(bmi)
print ("Your BMI is")
print (bmireal)