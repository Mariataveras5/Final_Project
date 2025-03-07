print("Welcome, Seeker! Step into the magic of tarot, where insight and guidance awaits. Open your heart, trust the cards, and let the journey begin!🌙🃏🔮")
name = input("What is your name? ")

def valid_intention(user_intention):
    """
    A function that validates whether the intention answered by the user is one of the 4 options
    :param user_intention: intention written by user
    :return: True if valid, otherwise False
    """
    intentions_files = {"relationships": "relationships_cards.py", "personal growth": "personal_growth_cards.py", "future": "future_cards.py","decision making": "decision_making_cards.py"}
    return user_intention in intentions_files

import relationship_cards
import future_cards
import personal_growth_cards
import decision_making_cards
import random

while True:
    intention = input(f"{name}, please choose one of the following intentions: relationships, personal growth, decision making or future: ").lower()
    intention = ' '.join(intention.split())
    if not valid_intention(intention):
        print("I'm sorry we do not offer those types of readings here. Please choose a valid intention.")
        continue

    n_cards = input("Lastly, choose whether you want a 3-card or a 5-card reading:")
    n_cards = int(n_cards)

    if n_cards == 3:
        if intention == "relationships":
            random_cards = random.sample(list(relationship_cards.cards.items()), 3)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "personal growth":
            random_cards = random.sample(list(personal_growth_cards.cards.items()), 3)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "decision making":
            random_cards = random.sample(list(decision_making_cards.cards.items()), 3)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "future":
            random_cards = random.sample(list(future_cards.cards.items()), 3)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

    elif n_cards == 5:
        if intention == "relationships":
            random_cards = random.sample(list(relationship_cards.cards.items()), 5)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "personal growth":
            random_cards = random.sample(list(personal_growth_cards.cards.items()), 5)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "decision making":
            random_cards = random.sample(list(decision_making_cards.cards.items()), 5)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

        elif intention == "future":
            random_cards = random.sample(list(future_cards.cards.items()), 5)
            for number, (card, description) in enumerate(random_cards, start=1):
                print(f"{number}. {card}: {description}")

    else:
        print("Invalid number of cards. Please choose either 3 or 5")
        continue

    another_reading= input("Would you like to explore another intention (yes/no)? ").lower()
    another_reading = ' '.join(another_reading.split())
    if another_reading=="no":
        print("Thank you for exploring your tarot reading. Goodbye!")
        break











