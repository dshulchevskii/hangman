from .game import Hangman
from random import choice


__version__ = '0.0.0'

if __name__ == '__main__':
    words = ['hello', 'world', 'python', 'ruby']
    word = choice(words)
    play = game.Hangman(word)
    play.run()
