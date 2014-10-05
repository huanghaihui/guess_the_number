"""
Rice_python : Guess the number
Author:Alex Huang
Data:4/10 2014
"""
#import simplegui
import random
import math
#input_guess

max_number = 100
min_number = 0
guess_times = 0

def input_guess(guess):
    global input_guess
    guess_number = guess
    str_guess = str(guess)
    print 'Guess was ' + str_guess

    if guess_number > secret_number:
        print 'Higher'
    elif guess_number < secret_number:
        print 'Lower'
    else:
        print 'Correct! You Win!'
        test()


def new_game():
    global secret_number
    global guess_times
    global max_number
    global min_number
    secret_number = random.randrange(min_number,max_number)
    guess_times = int(math.ceil(math.log(max_number - min_number + 1, 2)))
    print guess_times


def range100():
    global max_number
    max_number = 100
    new_game()

def range1000():
    global max_number
    max_number = 1000
    new_game()


def test():
    print 'Please choose range:100 or 1000'
    input_choose = input("Input_choose:" )
    if input_choose == 1000:
        range1000()
        print 'Here'
    else:
        range100()
    global guess_times
    while(guess_times>=0):
        input_guess_number = input("Input guess:")
        guess_times -= 1
        input_guess(input_guess_number)
    print 'Guess_times is over And You Lose!'

test()
