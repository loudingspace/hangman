# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

The project currently generates a random word from a word list with the generate_random_word() function. It then asks for user input using the ask_for_input() function inviting the user to enter a letter. If this is alphanumeric and only one character it then checks this using the check_guess(guess) function which checks to see if this letter is contained in the randomly generated word..

To run use python:

    python milestone_3.py
