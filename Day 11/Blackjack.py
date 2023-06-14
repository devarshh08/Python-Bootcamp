logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                
import random

def deal_card():
  #will allot random cards from deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  #returns total score of cards
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, Opponent has blackjack"
  elif user_score == 0:
    return "Congratulations, You win with a blackjack!"
  elif user_score > 21:
    return "You went over, you lose"
  elif computer_score > 21:
    return "Opponent went over, you win"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose"

def blackjack():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  print(logo)
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    print(" ")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      game_continue = input("Type 'y' to get another card, type 'n' to pass: ")
      if game_continue == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(" ")
  print(f"""Your final hand {user_cards}, your final score {user_score}
Opponent's final hand {computer_cards}, Opponent's final score {computer_score}""")
  print(compare(user_score, computer_score))
  print(" ")


while input("Do you want to play a game of blackjack? Type 'y' or 'n' \n") == 'y':
  blackjack()
else:
  pass