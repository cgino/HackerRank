# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.


import numpy as np


def start(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)
    print(m1, m2)

    for i in num1:
        #print('i:',i)
        #print(ord(i))
        #print(ord("0"))
        n1 += (ord(i) - ord("0")) * m1
       # print("n1:", n1)
        m1 = m1 // 10
        #print('m1:', m1)

    for i in num2:
        #print('i:', i)
        #print(ord(i))
        #print(ord("0"))
        n2 += (ord(i) - ord("0")) * m2
        #print("n2:", n2)
        m2 = m2 // 10
        #print('m2:', m2)

    return(n1+n2)

def sum(n1, n2):

    n1 = eval(n1)
    n2 = eval(n2)
    print(n1+n2)

if __name__ == '__main__':
    num1 = '321'
    num2 = '86554445529'

    start(num1, num2)
    print(start(num1, num2))

    sum(num1, num2)
