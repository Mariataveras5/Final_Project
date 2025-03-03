name=input("Welcome, what is your name?")
intention=input(f"{name}, please choose one of the following intentions: relationships, personal growth, decision making or future-")
try:
    n_cards=int(input("Lastly, choose whether you want a 3-card or a 5-card reading"))

except ValueError:
    print("I'm sorry we do not offer those readings, please select a valid option")


