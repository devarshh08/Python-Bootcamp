import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while True:
  print("Welcome to PyPassword Generator:")
  
  letters_length = int(input("How many letters would you like your password?\n"))
  symbol_length = int(input("How many symbols would you like?\n"))
  nums = int(input("How many numbers would you like?\n"))
  
  password = []
  
  for char in range(1, letters_length+1):
    password += random.choice(letters)
  for char in range(1,symbol_length+1):
    password += random.choice(symbols)
  for char in range(1, nums+1):
    password += random.choice(numbers)
  
  random.shuffle(password)
  
  print("Your password is:")
  for i in password:
    print(i, end ="")
  print("\n")

  ch = input("Enter 1 to exit, else any other key to continue:\n")
  
  print("\n")
  
  if ch == "1":
    break