# Given an array containing None values fill in the None values with most recent
# non None value in the array

import numpy as np

array1 = [1, None, 2, 3, None, None, 5, None]

print(array1[1] == None)

if array1[0] == 0: print("array must not start with None!")

for i in range(len(array1)):
    if array1[i] == None:
        array1[i] = array1[i - 1]

print(array1)

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 100
k = 50

interval = list(range(n - k, n))
# print(interval)


def prime_number(number, index=2):
    if int(np.sqrt(number)) + 1 == index:
        answer = True
    elif number % index == 0:
        answer = False
    else:
        answer = prime_number(number, index + 1)
    return answer


print(prime_number(7919))

primes = []
for ele in interval:
    # print("ele:", ele)
    # breakpoint()
    if prime_number(ele): primes.append(ele)
print(primes[-10:])

# filter with list comprehension

primes_filt = [x for x in interval if prime_number(x)]
print(primes_filt[-10:])




# Calculate the factorial for a given integer
num = 4

def factorial(number, res=1):
    if number < 0:
        return -1
    if number < 2:
        pass
    else:
        res = factorial(number - 1, res)*number
    return res


print(factorial(int(input("Please enter an integer"))))



#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.




