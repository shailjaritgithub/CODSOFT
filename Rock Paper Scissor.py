import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    def on_choice(user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        user_label.config(text=f"You chose: {user_choice.capitalize()}")
        computer_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        result_label.config(text=result)

        nonlocal user_score, computer_score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        score_label.config(text=f"Your score: {user_score} | Computer's score: {computer_score}")

    def play_again():
        user_label.config(text="")
        computer_label.config(text="")
        result_label.config(text="")
        user_score, computer_score = 0, 0
        score_label.config(text="Your score: 0 | Computer's score: 0")

    root = tk.Tk()
    root.geometry("600x600")
    root.configure(bg="pink")
    root.title("Rock-Paper-Scissors Game")


    # Add buttons for choices
    choices_frame = tk.Frame(root, bg='#81d8d0', bd=5)
    choices_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

    choices = ['rock', 'paper', 'scissors']
    for index, choice in enumerate(choices):
        choice_button = tk.Button(choices_frame, text=choice.capitalize(), bg="#febe98", font=('Arial', 12, 'bold'),
                                  command=lambda ch=choice: on_choice(ch))
        choice_button.grid(row=0, column=index, padx=10, pady=10)

    # Labels for displaying choices and result
    user_label = tk.Label(root, text="", font=('Arial', 14, 'bold'), bg='#d6bad4')
    user_label.place(relx=0.5, rely=0.3, anchor='n')

    computer_label = tk.Label(root, text="", font=('Arial', 14, 'bold'), bg='#b2e8e8')
    computer_label.place(relx=0.5, rely=0.4, anchor='n')

    result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'), bg='#ffe7bc')
    result_label.place(relx=0.5, rely=0.5, anchor='n')

    # Label for displaying scores
    user_score, computer_score = 0, 0
    score_label = tk.Label(root, text=f"Your score: {user_score} | Computer's score: {computer_score}",
                           font=('Arial', 12), bg='#dddddd')
    score_label.place(relx=0.5, rely=0.6, anchor='n')

    # Button to play again
    play_again_button = tk.Button(root, text="Play Again", bg='#ed9c84', font=('Arial', 12, 'bold'), command=play_again)
    play_again_button.place(relx=0.5, rely=0.7, anchor='n')

    root.mainloop()

# Start the game
play_game()
