import random
while True:
  user_choice = int(input("What do you choose?\nType 1 for Rock, 2 for Paper, 3 for Scissors, and 4 for EXIT\n"))
  comp_choice = random.randint(1,3)
  if user_choice == 1:
    print("""You chose Rock
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
  elif user_choice == 2:
    print("""You chose Paper
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)
  elif user_choice == 3:
    print("""You chose Scissors
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)
  elif user_choice == 4:
      print("Thank you for playing this game.")
      break
  else:
      print("Please enter a number from 1 to 4 (1,2,3,4).")
      continue
  if comp_choice == 1:
    print("""Computer chose Rock
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
  elif comp_choice == 2:
    print("""Computer chose Paper
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)
  elif comp_choice == 3:
    print("""Computer chose Scissors
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)
  
  if comp_choice == 1:
    if user_choice == 1:
      print("Draw")
    elif user_choice == 2:
      print("You win! Congratulations!")
    elif user_choice == 3:
      print("Computer wins")
  elif comp_choice == 2:
    if user_choice == 1:
      print("Computer wins")
    elif user_choice == 2:
      print("Draw")
    elif user_choice == 3:
      print("You win! Congratulations!")
  elif comp_choice == 3:
    if user_choice == 1:
      print("You win! Congratulations!")
    elif user_choice == 2:
      print("Computer wins")
    elif user_choice == 3:
      print("Draw")
  
  print(" ")
