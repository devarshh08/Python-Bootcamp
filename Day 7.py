#for this project you also need the hangman_art and hangman_words files

import random
import hangman_art
import hangman_words

#here we define these variables
game_over = False
lives = 6

#we are choosing a word from the wordlist
chosen_word = random.choice(hangman_words.wordlist)
word_length = len(chosen_word)

#this is an empty list to display the dashes
blanks = []
for i in range(word_length):
  blanks += "_"

print(hangman_art.logo)
print("")

#while game_over is false, this loop will keep looping
while not game_over:
  user_choice = input("Guess a letter: ").lower()
  
  #this is a cheatcode
  if user_choice == "display":
    print(f"{chosen_word}\n")
    lives+=1

  #this checks if user has already entered a letter guessed before
  if user_choice in blanks:
    print("You have already guessed it.\n")

  #this will allot each letter of chosen word to variable letter and will check it letter matches any of the user choice and if it matches, the letter will be added at the exact place in the blanks list
  for i in range(word_length):
    letter = chosen_word[i]
    if letter == user_choice:
      blanks[i] = letter

  #this will work when user enters the wrong word, and user will lost one life and other loop checks how many lives user has left; if user has 0 lives left it quits game
  if user_choice not in chosen_word:
    print("You Lost one life.\n")
    lives -= 1
    if lives == 0:
      game_over = True
      print("Game over\n")

  #this will print the list blanks in string form
  for i in blanks:
    print(i, end = "")

  #this will check if user has completed all stages
  if "_" not in blanks:
    game_over = True
    print("")
    print("Congratulations!!")
    print("You Win\n")

  print(hangman_art.stages[lives])
    