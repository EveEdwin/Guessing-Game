# Guessing-Game
Guessing Game a fun timepass game 

Here's a brief description:

1. **Imports:**
   - `import tkinter as tk`: Imports the Tkinter library and aliases it as `tk`.
   - `import random`: Imports the `random` module to generate a random number.

2. **`check_guess()` Function:**
   - Checks the user's input against the randomly generated number.
   - Compares the guessed number with the random number and provides feedback to the user based on the comparison.

3. **Random Number Generation:**
   - Generates a random number between 1 and 100 using `random.randint()`.

4. **Main Window Setup:**
   - Creates the main window titled "Number Guessing Game".
   - Includes a label prompting the user to guess the number and an entry field for the user's input.
   - Provides a button to check the user's guess.
   - Displays the result or feedback in a label below the entry field.

5. **Main Loop:**
   - Initiates the main event loop (`root.mainloop()`) to run the Tkinter application.

This code will create a simple and functional GUI for a number guessing game, allowing users to input their guesses and receive feedback based on their guesses compared to the randomly generated number.
