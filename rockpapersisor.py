import tkinter as tk
from tkinter import messagebox
import random

# --- Logic Layer ---
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    # Update the UI labels
    comp_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result, fg="#f39c12" if result == "It's a Tie!" else "#2ecc71" if "Win" in result else "#e74c3c")

# --- UI Layer ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x450")
root.config(bg="#2c3e50")

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#2c3e50", fg="#ecf0f1", pady=20)
title.pack()

# Instruction
inst = tk.Label(root, text="Choose your move:", font=("Arial", 12), bg="#2c3e50", fg="#bdc3c7")
inst.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=20)

# Button styling and creation
btn_style = {"font": ("Arial", 12, "bold"), "width": 10, "bd": 0, "cursor": "hand2", "activeforeground": "white"}

rock_btn = tk.Button(btn_frame, text="Rock", bg="#95a5a6", command=lambda: play("Rock"), **btn_style)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", bg="#ecf0f1", command=lambda: play("Paper"), **btn_style)
paper_btn.grid(row=0, column=1, padx=5)

sciss_btn = tk.Button(btn_frame, text="Scissors", bg="#bdc3c7", command=lambda: play("Scissors"), **btn_style)
sciss_btn.grid(row=0, column=2, padx=5)

# Display Area
comp_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1")
comp_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#2c3e50")
result_label.pack(pady=20)

# Reset Button
def reset():
    comp_choice_label.config(text="Computer chose: ")
    result_label.config(text="")

reset_btn = tk.Button(root, text="Reset Game", command=reset, bg="#34495e", fg="white", bd=0)
reset_btn.pack(side="bottom", pady=20)

root.mainloop()