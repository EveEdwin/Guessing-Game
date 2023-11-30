import tkinter as tk
import random

# Function to check the user input and compare with the randomly generated number
def check_guess():
    try:
        user_guess = int(entry.get())
        difference = abs(user_guess - random_number)

        if user_guess == random_number:
            result_label.config(text="Congratulations! You guessed it right!", fg="green")
        elif difference <= 5:
            result_label.config(text="Close! Try again.", fg="orange")
        elif user_guess < random_number:
            result_label.config(text="Too low! Try a higher number.", fg="blue")
        else:
            result_label.config(text="Too high! Try a lower number.", fg="red")
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="black")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Styling
root.geometry("350x200")
root.configure(bg="#f0f0f0")

# Fonts
font_label = ("Arial", 12)
font_result = ("Arial", 12, "bold")

# Label and Entry field for user input
label = tk.Label(root, text="Guess the number (between 1 and 100):", font=font_label, bg="#f0f0f0")
label.pack(pady=10)
entry = tk.Entry(root, font=font_label)
entry.pack()

# Button to check the guess
check_button = tk.Button(root, text="Check", command=check_guess, font=font_label, bg="#4CAF50", fg="white", padx=10)
check_button.pack(pady=10)

# Label to display the result or feedback
result_label = tk.Label(root, text="", font=font_result, bg="#f0f0f0")
result_label.pack()

# Run the application
root.mainloop()
