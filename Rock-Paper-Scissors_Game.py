import tkinter as tk
import random

user_score = 0
computer_score = 0
max_score = 3  

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        user_score += 1
        if user_score == max_score:
            return "You win the game!"
        return "You win this round!"
    else:
        computer_score += 1
        if computer_score == max_score:
            return "Computer wins the game!"
        return "Computer wins this round!"

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score: User 0 - 0 Computer")
    result_label.config(text="")

def user_choice_handler(choice):
    if user_score < max_score and computer_score < max_score:
        computer_choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(computer_choices)

        result = determine_winner(choice, computer_choice)

        user_label.config(text=f"Your choice: {choice}")
        computer_label.config(text=f"Computer's choice: {computer_choice}")
        result_label.config(text=result)
        score_label.config(text=f"Score: User {user_score} - {computer_score} Computer")
    else:
        if user_score == max_score:
            result_label.config(text="You have already won the game!")
        elif computer_score == max_score:
            result_label.config(text="Computer has already won the game!")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

root.geometry("400x350")

user_label = tk.Label(root, text="Your choice:", font=("Helvetica", 14))
computer_label = tk.Label(root, text="Computer's choice:", font=("Helvetica", 14))
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
score_label = tk.Label(root, text="Score: User 0 - 0 Computer", font=("Helvetica", 14))

user_label.pack(pady=5)
computer_label.pack(pady=5)
result_label.pack(pady=10)
score_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

new_game_frame = tk.Frame(root)
new_game_frame.pack(pady=30)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice_handler("rock"), font=("Helvetica", 12),
                        bg="red", padx=20, pady=10)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice_handler("paper"), font=("Helvetica", 12),
                         bg="blue", padx=20, pady=10)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice_handler("scissors"), font=("Helvetica", 12),
                            bg="yellow", padx=20, pady=10)

rock_button.pack(side="left", padx=20)
paper_button.pack(side="left", padx=20)
scissors_button.pack(side="left", padx=20)

new_game_button = tk.Button(new_game_frame, text="Play New Game", command=reset_scores, font=("Helvetica", 12),
                            bg="black", fg="white", padx=20, pady=10)
new_game_button.pack()

root.mainloop()
