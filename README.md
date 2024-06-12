# Hangman Bot

This is a Telegram bot for playing the classic game of Hangman. The bot allows users to play Hangman by guessing letters to complete a word.

## Features

- Start a new game by typing `/play`.
- ASCII art representation of the hangman.
- Image-based representation of the hangman.
- Keeps track of used letters and the current state of the word.
- Provides feedback on invalid inputs.
- Congratulates the user on guessing the word correctly.
- Informs the user if they have lost the game.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hangman-bot.git
    cd hangman-bot
    ```

2. Install the required packages:
    ```bash
    pip install pyTelegramBotAPI
    ```

3. Add your Telegram bot token:
    Replace the placeholder `'Token_id'` in the script with your actual Telegram bot token.

4. Run the bot:
    ```bash
    python hangman_bot.py
    ```

## How to Play

1. Start the bot by sending `/start` or `/help` to the bot in a Telegram chat.
2. Begin a new game by sending `/play`.
3. Guess letters by sending a single letter in a message.
4. The bot will respond with the current state of the word, used letters, and an updated hangman image.
5. Continue guessing until you either guess the word correctly or run out of attempts.

## Code Overview

The main components of the bot are:

- **Reading words from a file:** The bot reads words from a file named `new.txt`. If the file is not found, it uses a default list of words.
- **Hangman ASCII art:** ASCII art is used to represent the hangman at different stages of the game.
- **Game state management:** The bot keeps track of the game state for each user, including the word to be guessed, the current state of the guessed word, the number of wrong guesses, and the letters that have been used.
- **Message handlers:** The bot includes handlers for `/start`, `/help`, and `/play` commands, as well as a handler for processing guessed letters.
- **Displaying the game state:** The bot sends messages and images to the user to display the current state of the game.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for providing the Python interface for the Telegram Bot API.
