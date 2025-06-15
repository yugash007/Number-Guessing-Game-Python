# 🎮 Number Guessing Game (Python)

This is a simple console-based number guessing game written in Python. The player selects a difficulty level, and then tries to guess the number randomly selected by the computer within a limited number of attempts.

## 🚀 How to Play

1. When the program starts, you will be prompted to select a difficulty level:
   - **E** for Easy (0–10, 5 attempts)
   - **M** for Medium (0–50, 10 attempts)
   - **H** for Hard (0–100, 15 attempts)

2. The game will then generate a random number within the chosen range.

3. Enter your guesses one by one.

4. After each guess, you'll be given a hint:
   - "It's too low"
   - "It's too high"
   - "Congratulations! You guessed it correctly" if you get it right

5. The game ends when you guess the correct number or run out of attempts.

## 🧠 Game Logic

- The program uses Python's built-in `random` module to generate the number.
- It validates user input to ensure it's numeric and within bounds.
- Global variables are used to manage state like number of tries and win status.

## 🛠️ Requirements

- Python 3.x
  
##📝 Features
- Input validation
- Multiple difficulty levels
- Dynamic feedback based on guesses
- Replay logic (coming soon or can be added)

## 📦 Run the Program

```bash
python number_guessing_game.py
````
