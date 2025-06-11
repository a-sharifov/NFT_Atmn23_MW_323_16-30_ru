import random
import time

def is_win(player_1, player_2):
    return player_1 == "к" and player_2 == "н" \
                or player_1 == "н" and player_2 == "б" \
                or player_1 == "б" and player_2 == "к"

def slow_print(text, s):
    for i in text:
        time.sleep(s)
        print(i, end="")
    print()

actions = ["к", "н", "б"]
def game():
    while True:
        bot_choice, user_choice = random.choice(actions), input("select: к - камень, н - ножницы, б - бумага: ")
        if user_choice not in actions: slow_print("is not correct...", 0.2)
        print("Bot win") if is_win(bot_choice, user_choice) \
            else print("User Win") if is_win(bot_choice, user_choice) else print("draw")

game()
