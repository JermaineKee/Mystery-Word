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


# def difficulty():
#     diff = input("ENTER easy, medium, or hard to decide the difficulty.")
#     if diff == 'easy':
#         game_word = random_word(easy_words(word_list))
#
#     elif diff == 'medium':
#         game_word = random_word(medium_words(word_list))
#     else:
#         game_word = random_word(hard_words(word_list))
#
#     return game_word


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
    for letter in word:
        if letter not in guesses:
            return False
    return True


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:"""

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
    guessed = []
    print('Your word has {} letters'.format(len(game_word)))
    while attempts > 0 and is_word_complete(game_word, guessed) == False:
        print(display_word(game_word, guessed))
        print('{} guesses to go'.format(attempts))
        print(guessed)
        while True:
            rec_letter = input('Guess a letter: ').lower()
            if rec_letter in guessed:
                print('No duplicate letters please.')
                continue
            elif len(rec_letter) > 1:
                print('Just one letter please.')
                continue
            elif rec_letter.isalpha() != True:
                print ('Just letters please.')
                continue
            elif rec_letter in game_word:
                guessed.append(rec_letter)
                print('Right On!')
                break
            elif rec_letter not in game_word:
                print('Nope!')
                attempts -= 1
                guessed.append(rec_letter)
                break
            else:
                continue

        if attempts <= 0:
            new_game = input(('Nice Try. The word was {}. \n Enter (Y)es to play again: '.format(game_word)))
            if new_game == 'yes':
                return main()
            else:
                exit()
        else:
            new_game = input('Good Job! \n Enter (Y)es to play again: ')
            if new_game == 'yes':
                return main()
            else:
                exit()






#new_game = True
#while new_game:
    #new_try = input("Want to try again? (Y) or (N): ")
    #if new_try[0] in ('Y', 'y'):
        #print("Let's Play!")
        #new_game = True
    #else:
    #    print("Ok, Goodbye")
    #    new_game = False


if __name__ == '__main__':
        main()
