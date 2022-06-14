#!/usr/bin/env python
import prompt

def welcome_user(game_name):
  name = prompt.string("May I have your name?")
  print(str("Hello {name}!\n{game_name}"))
  return name


  
#   while name == ' ':
#     print('May I have your name? ', end='')
#     name = input()
#     print(f'Hello, {name}!')

# welcome_user(name = ' ')