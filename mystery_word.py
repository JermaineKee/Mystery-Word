import random
import re

word_bank = open("/usr/share/dict/words")
dictionary = word_bank.read()
dictionary = dictionary.split()


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_list = []
    for word in easy_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
    return easy_list



def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_list = []
    for word in medium_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_list.append(word)
    return medium_list


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_list = []
    for word in hard_list:
        if len(word) > 7:
            hard_list.append(word)
    return hard_list


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return random.choice(word_list)



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
    for letter in word:
        if letter in guesses:
            word_display.append(letter)
        else:
            word_display.append('_')

    return word_display

def difficulty():
    diff = input("ENTER easy, medium, or hard to decide the difficulty.")
    if diff == 'easy':
        game_word = random_word(easy_words(dictionary))
    elif diff == 'medium':
        game_word = random_word(medium_words(dictionary))
    else:
        game_word = random_word(hard_words(dictionary))

    return game_word







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


def game_loop(game_word):

def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:"""

if __name__ == __’main’__:
	main()
