#!/usr/bin/env python

from brain_games.cli import welcome_user



def greet(where):
    print('Welcome to the {}!'.format(where))

def main():
    greet('Brain Games')

if __name__ == '__main__':
    main()