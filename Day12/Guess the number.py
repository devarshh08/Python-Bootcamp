logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  """

"""If you are reading the code, there is a cheatcode. enter cheatcode in difficulty and you get the answer"""
import random

def guess_the_number(user_choice, guessed_number):
  global n
  if user_choice > guessed_number:
    return "Too high"
  elif user_choice < guessed_number:
    return "Too low"
  elif user_choice == guessed_number:
    return f"You got it! the answer was {guessed_number}"
    
print(logo)
print(" ")
guessed_number = random.randint(1, 100)
print("Welcome to the number guessing game!\n")
print("I am thinking of a number between 1 and 100.\n")
difficulty = input("Choose a difficulty, type easy or hard: ")


if difficulty == 'easy':
  n = 10
  for i in range(n):
    print(f"You have {n} attempts left to guess the number:")
    user_choice = int(input("Make a guess: "))
    n -= 1
    print(guess_the_number(user_choice, guessed_number))
    if user_choice == guessed_number:
      break

elif difficulty == 'hard':
  n = 5
  for i in range(n):
    print(f"You have {n} attempts left to guess the number:")
    user_choice = int(input("Make a guess: "))
    n -= 1
    print(guess_the_number(user_choice, guessed_number))
    if user_choice == guessed_number:
      break
    
if difficulty == 'cheatcode':
  print(guessed_number)
  n = 5
  for i in range(n):
    print(f"You have {n} attempts left to guess the number:")
    user_choice = int(input("Make a guess: "))
    n -= 1
    print(guess_the_number(user_choice, guessed_number))
    if user_choice == guessed_number:
      break

