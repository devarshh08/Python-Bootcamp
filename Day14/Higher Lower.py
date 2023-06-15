import random
from game_data import data
from art import logo, vs

game_over = False
score = 0

while not game_over:
    dict_persona_1 = random.choice(data)
    name_person1 = dict_persona_1["name"]
    followers1 = dict_persona_1["follower_count"]
    description_person1 = dict_persona_1["description"]
    country_person1 = dict_persona_1["country"]

    dict_persona_2 = random.choice(data)
    name_person2 = dict_persona_2["name"]
    followers2 = dict_persona_2["follower_count"]
    description_person2 = dict_persona_2["description"]
    country_person2 = dict_persona_2["country"]

    if followers1 > followers2:
        higher = "A"
    else:
        higher = "B"

    print(f"{logo}\n")
    print(f"Compare A: {name_person1}, {description_person1}, from {country_person1}\n")
    print(f"{vs}\n")
    print(f"Against B: {name_person2}, {description_person2}, from {country_person2}\n")
    user_ch = input("Who has more followers? Type 'A' or 'B': ")

    if user_ch == higher:
        score += 1
    elif user_ch == "cheatcode":
        print(f"Followers of A are {followers1} and Followers of B are {followers2}")
        score += 1
    elif user_ch != higher:
        print(f"Sorry that's wrong, Final score: {score}")
        game_over = True
        break