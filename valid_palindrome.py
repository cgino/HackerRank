# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

import numpy as np

s1 = 'radkar'
s2 = 'adsfasdf'

def palindrome_check(input):
    """
    A palindrome is a symmetric word. This function takes the input string and checks if it is palindromic.
    :param input: string
    :return: bool
    """

    # if len(input) % 2 == 0:
    for i in range(len(input)//2):
        # print(input[i], input[-i-1])
        if not input[i] == input[-i-1]:
            return False
    return True
    # else:

def char_killer(input, pos):
    """
    Removes a single char from a given input string
    :param input: string
    :param pos: int
    :return: string
    """
    return input[:pos]+input[1+pos:]

def reduced_palindrome(input):
    for i in range(len(input)):
        if palindrome_check(char_killer(input, i)):
            return input, "is a palindrome after removing one char"

    return input, "is can't be made into a palindrome with removing one char"


if __name__ == "__main__":
    s1 = 'radkafr'
    s2 = 'adsfasdf'
    # print(palindrome_check('radar'))
    char_killer('radar', 2)

    if not palindrome_check(s1):
        print(reduced_palindrome(s1))
    else:
        print(s1, "is a palindrome")


