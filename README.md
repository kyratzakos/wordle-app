# Wordle Game

This is a simple implementation of the Wordle game in Python. In this game, the player needs to guess a 5-letter word, and the program will provide feedback on the correctness of each letter in the guessed word.

## Requirements

To run this game, you need to have the following dependencies installed:

-   `RandomWords`: A Python library from [tomislater](https://github.com/tomislater) to generate random English words ([GitHub Repo](https://github.com/tomislater/RandomWords)).
-   `rich`: A Python library for rich text and beautiful formatting in the terminal.

You can install these dependencies by running:

```
pip install -r requirements.txt
```

## How to Play

1. Clone this repository to your local machine.
2. Install the dependencies as mentioned above.
3. Run the `wordle.py` script using Python:

```
python wordleapp.py
```

4. The game will prompt you to enter a 5-letter word.
5. Keep guessing words until you correctly guess the word or exhaust your allowed guesses.
6. The program will provide feedback on each guess, indicating correct letters in the correct position, correct letters in the wrong position, and incorrect letters.
7. The game ends when you correctly guess the word or use all allowed guesses.

Have fun playing Wordle!
