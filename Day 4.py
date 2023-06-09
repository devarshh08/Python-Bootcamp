import random


def hand_gestures(n):
    if n == 1:
        print("""Rock
              _______
          ---'   ____)
                (_____)
                (_____)
                (____)
          ---.__(___)
          """)
    elif n == 2:
        print("""Paper
               _______
          ---'    ____)____
                     ______)
                    _______)
                   _______)
          ---.__________)
          """)
    elif n == 3:
        print("""Scissors
              _______
          ---'   ____)____
                    ______)
                 __________)
                (____)
          ---.__(___)
          """)


while True:
    user_choice = int(input("What do you choose?\nType 1 for Rock, 2 for Paper, 3 for Scissors, and 4 for EXIT\n"))
    comp_choice = random.randint(1, 3)

    if user_choice == 4:
        print("Thank you for playing this game.")
        break
    elif user_choice < 1 or user_choice > 4:
        print("Please enter a number from 1 to 4 (1,2,3,4).")
        continue

    print("You chose", end=" ")
    hand_gestures(user_choice)

    print("Computer chose", end=" ")
    hand_gestures(comp_choice)

    if comp_choice == user_choice:
        print("Draw")
    elif comp_choice + user_choice == 4:
        if comp_choice < user_choice:
            print("Computer wins")
        else:
            print("You win! Congratulations!")
    else:
        if comp_choice > user_choice:
            print("Computer wins")
        else:
            print("You win! Congratulations!")

    print(" ")
