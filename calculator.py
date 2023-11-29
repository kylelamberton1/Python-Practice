from art import logo
#ADD
def add(n1,n2):
  return n1+n2
#SUBTRACT
def subtract(n1,n2):
  return n1-n2
#MULTIPLY
def multiply(n1,n2):
  return n1*n2
#DIVIDE
def divide(n1,n2):
  return n1/n2

calc_ops = {
  "+": add,
  "-":subtract, 
  "*":multiply, 
  "/":divide
}
def calculator():
  print (logo)
  num1 = float(input("What's the first number?: "))
  for symbol in calc_ops:
    print (symbol)
  continue_calc = True

  while continue_calc:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = calc_ops[operation_symbol]
    answer = calculation_function(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
      num1 = answer
    else:
      continue_calc = False  
      calculator()

calculator()


# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = calc_ops[operation_symbol]
# #Here the code will be:
# #second_answer = multiply(multiply(num1, num2), num3)
# second_answer = calculation_function(calculation_function(num1, num2), num3)
# #second_answer = 2 * 3 * 3 = 18
# #To fix this bug we need to change the code on line 42 to:
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
