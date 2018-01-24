# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:41:34 2017

@author: naveen84
"""

print("Please think of a number between 0 and 100!")
l = 0
h = 100
ans = 'a'
while ans != "c":
    guess = (l+h)//2
    print("Is your secret number ",end='')
    print(guess,end='')
    print('?')
    while True:
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if ans != 'c' and ans!= 'h' and ans != 'l':
            print('Sorry, I did not understand your input.')
            print("Is your secret number ",end='')
            print(guess,end='')
            print('?')
        else:
            break
    if ans == 'h':
        h = guess
    elif ans == 'l':
        l = guess
print('Game over. Your secret number was: '+ str(guess))
    