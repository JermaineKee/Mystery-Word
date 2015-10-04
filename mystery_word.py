import random
import re


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
    return easy_list


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_list.append(word)
    return medium_list


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_list = []
    for word in word_list:
        if len(word) > 7:
            hard_list.append(word)
    return hard_list


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    myst_word = random.choice(word_list)
    return myst_word


def difficulty():
    diff = input("ENTER easy, medium, or hard to decide the difficulty.")
    if diff == 'easy':
        game_word = random_word(easy_words(word_list))

    elif diff == 'medium':
        game_word = random_word(medium_words(word_list))
    else:
        game_word = random_word(hard_words(word_list))

    return game_word


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    word_display = []
    for guess in word:
        if guess in guesses:
            word_display.append(guess)
        else:
            word_display.append('_')

    word_display = ' '.join(word_display).upper()
    return word_display


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    attempts = display_word(word, guesses)
    if '_' in attempts:
        return False
    else:
        return True


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:"""
    word_list = []
    with open("/usr/share/dict/words") as word_bank:
        word_list = word_bank.read()
        word_list = word_list.split()

    diff = input("ENTER easy, medium, or hard to decide the difficulty. \n Enter quit, to quit")
    if diff == 'easy':
            game_word = random_word(easy_words(word_list))
            print('You chose easy!')
    elif diff == 'medium':
        game_word = random_word(medium_words(word_list))
        print('You chose medium!')
    elif diff == 'hard':
        game_word = random_word(hard_words(word_list))
        print('You chose hard!')
    elif diff == 'quit':
        print('Adios Quitter!')
        exit()
    else:
        print('Not acceptable response, try again')
        return main()

    attempts = 8
    guessed = [
    print('Your word has {} letters'.format(len(game_word)))
    ]




new_game = True
while new_game:
    new_try = input("Want to try again? (Y) or (N): ")
    if new_try[0] in ('Y', 'y'):
        print("Let's Play!")
        new_game = True
    else:
        print("Ok, Goodbye")
        new_game = False


if __name__ == '__main__':
        main()
