import  tkinter as tk
import random
from functools import partial


def game(choice):
    text_result = ""
    bot_choice = random.choice(["rock", "paper", "scissors"])

    if choice == "paper" and bot_choice == "rock" \
        or choice == "rock" and bot_choice == "scissors" \
        or choice == "scissors" and bot_choice == "paper":
            text_result = "user win"

    elif bot_choice == "paper" and choice == "rock" \
            or bot_choice == "rock" and choice == "scissors" \
            or bot_choice == "scissors" and choice == "paper":
        text_result = "bot win"

    else: text_result = "draw"
    result.config(text=text_result, fg="blue")



root = tk.Tk()
root.title("Rock paper scissors")
root.geometry("300x200")


result = tk.Label(root)
result.pack(pady=20)

button_rock = tk.Button(
    root,
    text="rock",
    width="100",
    height="2",
    background="green",
    fg="white",
    borderwidth="0",
    command=partial(game, "rock"))


button_rock.pack()

button_paper = tk.Button(
    root,
    text="paper",
    width="100",
    height="2",
    bg="blue",
    fg="white",
    borderwidth="0",
    command=partial(game, "paper"))
button_paper.pack()

button_scissors = tk.Button(
    root, text="scissors", width="100", height="2", bg="purple", fg="white", borderwidth="0", command=partial(game, "scissors"))
button_scissors.pack()

root.mainloop()
