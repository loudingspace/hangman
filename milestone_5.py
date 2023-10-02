import random


class Hangman:
    '''
    This class represents a game of Hangman

    Attributes:
        word (string): a word picked at random from word_list
        word_guessed (list): a representation of the word with undescores for letters not guessed
        num_letters (int): the number of unique letters in word
        word_list (list): the supplied list of words from which word is picked at random
        list_of_guesses(list): a list of letters of all the guesses which the user has made
    '''

    def __init__(self, word_list, num_lives=5):
        '''
        Initialise the class with a supplied word list and an optional num_lives

        Args:
            word_list (list): a list of words to be guessed
            num_lives (int): an optional number of lives, defaults to 5
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Checks the guessed letter again the current randomly selected word

        Args:
            guess (string): a letter to be evaluated against the value of the current word
        '''

        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        '''
        Asks the user for input.

        This consists of a While loop that will keep asking the user for input. It calls the check_guess method on the current instantiation of the class.
        '''
        # while True: <-- the loop is now from the play_game method
        guess = input('Please guess a single letter: ')

        if not (len(guess) == 1 and guess.isalpha()):
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)

        self.list_of_guesses.append(guess)


def play_game(word_list):
    '''
    This runs the game when called

    Args:
        word_list (list): a list of words

    A while loop runs asking the player for guesses of the word. If the player guesses the word or if they run out of lives, the game ends.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            print(
                f'\nWord to guess: {" ".join(game.word_guessed)}\tLives left: {game.num_lives}')
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

    play_again = input(
        '\nThank you for playing. Would you like to play again? ')
    if play_again[0].lower() == 'y':
        play_game(word_list)
    else:
        print('\nHave a great day!')


# Begin of main program:
word_list = ['grapes', 'orange', 'plum', 'kiwi', 'banana']
play_game(word_list)
