# Hangman Game (CLI)

A classic, interactive Command Line Interface (CLI) implementation of the traditional Hangman game built using Python. The application handles dynamic state tracking, robust user input cleaning, duplicate guess prevention, and visual feedback using ASCII art gallows.

This project is part of a comprehensive Java and Python-based multi-game suite developed from scratch.

## 🚀 Features

* **Dynamic Visuals:** Renders real-time ASCII art gallows (`HANGMAN_PICS`) that evolve with every incorrect guess.
* **Robust Input Cleaning:** Validates user inputs to reject symbols, numbers, or multiple characters instantly without losing a turn.
* **Duplicate Guess Management:** Tracks and blocks previously guessed letters, warning the user instead of penalizing their remaining attempts.
* **Modular Architecture:** Cleanly separates asset data (word lists, alphabet validation) and graphical layouts from the core game execution loop.

## 🛠️ Project Structure

* `main.py` — The core execution engine containing the game logic loop and state tracking algorithms.
* `lists.py` — Contains asset arrays including the target word database (`hangman_words`), character tracking registers (`already_guessed`), and valid input boundaries (`small_alphabets`).
* `pics.py` — Holds the indexed ASCII art configurations (`HANGMAN_PICS`) representing the step-by-step states of the gallows.

## 🏃 Getting Started

### Prerequisites
Make sure you have Python 3 installed on your system.

### Installation & Run

1. Clone this repository:
   ```bash
   1.git clone [https://github.com/awabmosama-sketch/Hangman-Game-In-Python-CLI-.git](https://github.com/awabmosama-sketch/Hangman-Game-In-Python-CLI-.git)

   2.Navigate to the project directory:
   cd Hangman-Game-In-Python-CLI-

   3.Run the application:
   python main.py
🎮 Game Rules
The system selects a hidden word at random from the database.

You have a total of 6 incorrect attempts before the game ends.

Guessing correct letters reveals their positions in the hidden word.

Inputting invalid characters or duplicate letters will trigger a warning message but will not penalize your remaining tries.
