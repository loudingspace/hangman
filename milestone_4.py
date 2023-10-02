import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed_list = ['_' for letter in word]
        self.num_letters = len(set(list(word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):

        guess = guess.lower()

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            return True
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            return False

    def ask_for_input(self):
        while True:
            guess = input('Please guess a single letter: ')

            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                check_guess(guess)

            self.list_of_guesses.append(guess)

            # if len(guess) == 1 and guess.isalpha():  # the check is to see if it is valid,
            #     break
            # else:
            #     print('Invalid letter. Please, enter a single alphabetical character.')

        check_guess(guess)


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
word_guessed_list = ['_' for letter in word]
num_letters = len(set(list(word)))


hangman = Hangman(word_list)

hangman.ask_for_input()

# print(hangman.list_of_guesses, hangman.word, hangman.word_guessed_list,
#       hangman.num_letters, hangman.num_lives)

# print(word, word_guessed_list, num_letters)
# ask_for_input()
