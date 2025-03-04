name = input("Welcome, what is your name? ")
intention = input(f"{name}, please choose one of the following intentions: relationships, personal growth, decision making or future: ")

#change this into a function with docstring
intentions_files = {"relationships": "relationships_cards.py", "personal growth": "personal_growth_cards.py", "future": "future_cards.py","decision making": "decision_making_cards.py"}
if intention not in intentions_files:
    print("Invalid intention. Please restart and choose a valid option.")
    exit()

n_cards = input("Lastly, choose whether you want a 3-card or a 5-card reading:")
n_cards = int(n_cards)

import relationship_cards
import future_cards
import personal_growth_cards
import decision_making_cards
import random
if n_cards == 3:
    if intention == "relationships":
        random_cards = random.sample(list(relationship_cards.cards.items()), 3)
        for item in random_cards:
            print(item)

    elif intention == "personal growth":
        random_cards = random.sample(list(personal_growth_cards.cards.items()), 3)
        for item in random_cards:
            print(item)

    elif intention == "decision making":
        random_cards = random.sample(list(decision_making_cards.cards.items()), 3)
        for item in random_cards:
            print(item)

    elif intention == "future":
        random_cards = random.sample(list(future_cards.cards.items()), 3)
        for item in random_cards:
            print(item)


if n_cards == 5:
    if intention == "relationships":
        random_cards = random.sample(list(relationship_cards.cards.items()), 5)
        for item in random_cards:
            print(item)

    elif intention == "personal growth":
        random_cards = random.sample(list(personal_growth_cards.cards.items()), 5)
        for item in random_cards:
            print(item)

    elif intention == "decision making":
        random_cards = random.sample(list(decision_making_cards.cards.items()), 5)
        for item in random_cards:
            print(item)

    elif intention == "future":
        random_cards = random.sample(list(future_cards.cards.items()), 5)
        for item in random_cards:
            print(item)

else: #change into outro message
    exit()








