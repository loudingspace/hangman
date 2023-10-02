import random

word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']


def generate_random_word(word_list):
    '''
    args: a list of words

    return: a word from that list
    '''
    return random.choice(word_list)


def check_guess(guess):
    '''
    Checks the guess inputted by user

    arg guess:    a letter
    return: boolean whether letter in word
    '''

    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False


def ask_for_input():
    while True:
        guess = input('Please guess a single letter: ')
        if len(guess) == 1 and guess.isalpha():  # the check is to see if it is valid,
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)


word = generate_random_word(word_list)
print(word)
ask_for_input()
