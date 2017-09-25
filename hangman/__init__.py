from .game import Hangman
from random import choice


words = ['hello', 'world', 'python', 'ruby']


def play_hangman():
    word = choice(words)
    play = Hangman(word)
    play.run()
