#!/bin/python3

"""
1. Palindrome Checker
Write a function that checks if a given string is a palindrome (reads the same forwards and backward).
examples are: madam, racecar, reconocer, luzazul
"""

word = input(f"Please write the word and press enter: \n")

def palindrome_check(word):
    # sanitize word
    word = word.lower().strip()
    # invert word
    inversed_word = word[::-1]

    if word  == inversed_word [-1:]:
        print(f"The word '{word}' is a palindrome")
    else:
        print(f"Word '{word}' is not a palindrome")


if __name__ == "__main__":
    palindrome_check(word)
