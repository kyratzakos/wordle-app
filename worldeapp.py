from random_words import RandomWords
from rich import *

DOTS = {
    'correct_place': f'[black on green]o[/]',
    'correct_letter': f'[black on yellow]o[/]',
    'incorrect_letter': f'[black on white]o[/]'
}


def getaword():
    # generates a valid 5-letter word
    rw = RandomWords()
    validword = rw.random_words(min_letter_count=5)
    while len(validword[0]) != 5:
        validword = rw.random_words(min_letter_count=4)
    return validword


def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def game_is_over(guess, word, guesses, rounds):
    # checks if the game is over
    if guess == word or guesses == rounds:
        return True
    return False


def guess_check(guess_word, correct_word):
    # checks if the guess is correct letter per letter
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess_word):
        if correct_word[i] == guess_word[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(DOTS['correct_place'])
        elif letter in correct_word:
            guessed += correct_letter(letter)
            wordle_pattern.append(DOTS['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(DOTS['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def play():
    # main funtion of the game
    tries = 0
    word = getaword()
    while not game_is_over() :
        tries += 1
        g

    print(word)


if __name__ == '__main__':
    play()
