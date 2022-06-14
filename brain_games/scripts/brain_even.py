from ..cli import welcome_user
from random import randint
import prompt


def is_even():
    name = welcome_user("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    while count < 3:
        number = randint(0, 100)
        print(f'Question: {number}')
        while True:
            answer = input('Your answer: ')
            if answer == 'yes':
                if number % 2 == 0:
                    print('Correct!')
                    count += 1
                    break
                else:
                    count = 0
                    print(f"yes' is wrong answer. Correct answer was 'no'.\nLet's try again {name}")
                    break
            elif answer == 'no':
                if number % 2 == 1:
                    print('Correct!')
                    count += 1
                    break
                else:
                    count = 0
                    print(f"yes' is wrong answer. Correct answer was 'no'.\nLet's try again {name}")
                    break
            else:
                count = 0
                print(f"You can write only 'yes' or 'mo'.\nLet's try again {name}")
                break
    print(f'Congratulations!')


def main():
    is_even()


if __name__ == '__main__':
  main()