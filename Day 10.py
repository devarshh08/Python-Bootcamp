import os

def add(num1, num2):
  return (num1+num2)

def subtract(num1, num2):
  return (num1-num2)

def multiply(num1, num2):
  return (num1*num2)

def divide(num1, num2):
  return (num1/num2)

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,
}

def calculator():
  print("CALCULATOR\n")
  
  num1 = float(input("What is the first number?: "))
  for keys in operations:
    print(keys)
  
  continue_calc = True
  
  while continue_calc:
    operation = input("Pick an operation : ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation]
    answer = calculation_function(num1, num2) 
    
    print(f"{num1} {operation} {num2} = {answer}\n\n")
  
    redo = input(f"Type 'y' to continue calculating with {answer} \nor\ntype 'n' to exit \nor\ntype 'rd' to start a new calculation\n: ")
    
    if redo == 'y':
      num1 = answer
    elif redo == 'n':
      continue_calc = False
    elif redo == 'rd':
      calculator()

calculator()