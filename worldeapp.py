from random_words import RandomWords
from rich.prompt import Prompt
from rich.console import Console
from rich import *

DOTS = {
    'correct_place': f'[black on green]o[/]',
    'correct_letter': f'[black on yellow]o[/]',
    'incorrect_letter': f'[black on white]o[/]'
}

GUESS_STATEMENT = 'Enter a 5-letter word: '
ALLOWED_GUESSES = 6


def getaword():
    # generates a valid 5-letter word
    rw = RandomWords()
    validword = rw.random_words(min_letter_count=5)
    while len(validword[0]) != 5:
        validword = rw.random_words(min_letter_count=4)
    return validword[0]


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
    guessed = []
    wordle_pattern = []
    correct_letters = set(correct_word)
    
    for i, letter in enumerate(guess_word):
        if correct_word[i] == letter:
            guessed += correct_place(letter)
            wordle_pattern.append(DOTS['correct_place'])
        elif letter in correct_letters:
            guessed += correct_letter(letter)
            wordle_pattern.append(DOTS['correct_letter'])
            correct_letters.remove(letter)
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(DOTS['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)



def play():
    # main funtion of the game
    end_of_game = False
    word = getaword()
    already_guessed = []
    all_words_guessed = []
    full_wordle_pattern = []
    print(word)
    
    while not end_of_game :
        guess = Prompt.ask(GUESS_STATEMENT).lower()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = guess_check(guess, word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and guess != word:
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Correct Word: {word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    console = Console()
    play()
