import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("450x350")
root.configure(bg="#222222")  # Set a dark background color for the main window

# Choices for the game
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(player_choice):
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    # Display the result
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}", fg="white")

# Layout for buttons and result display
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg="#222222", fg="cyan")
title_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#222222")
button_frame.pack(pady=10)

# Create buttons for each choice with distinct colors
rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock"), bg="#007ACC", fg="white")
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper"), bg="#FF5722", fg="white")
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors"), bg="#4CAF50", fg="white")
scissors_button.grid(row=0, column=2, padx=5)

# Display result with a distinct color
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), bg="#222222", fg="white")
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
