from random_words import RandomWords


# faction that generates a valid word
def getaword():
    rw = RandomWords()
    validword = rw.random_words(min_letter_count=5)
    print(f'Word is: {validword}')

    while validword is None or '-' in validword:
        validword = rw.random_words(min_letter_count=5).upper()
    else:
        print(f'Word is: {validword}')
        return validword


# main faction of the game
def play():
    word = getaword()
    print(word)


if __name__ == '__main__':
    play()