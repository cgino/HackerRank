# Neo has a complex matrix script. The matrix script is a X
# grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
# Neo reads the column from top to bottom and starts reading from the leftmost column.
# If there are symbols or spaces between two alphanumeric characters of the decoded script,
# then Neo replaces them with a single space '' for better readability.
# Neo feels that there is no need to use 'if' conditions for decoding.
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
# Input Format
# The first line contains space-separated integers
# (rows) and (columns) respectively.
# The next lines contain the row elements of the matrix script.
#
# Constraints
# Note: A
# score will be awarded for using 'if' conditions in your code.
# Output Format
#
# Print the decoded matrix script.
#
# Sample Input 0
#
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
#
# Sample Output 0
#
# This is Matrix#  %!


#!/bin/python3

import re

# basic test input for sake of example
dim_input = '7 3'
txt_input = 'Tsi\nh%x\ni #\nsM \n$a #t%\nir!'

# reads-in input dimensions
# first_multiple_input = input().rstrip().split() # original input function
first_multiple_input = dim_input.rstrip().split()  # adapted input function for sake of example
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

# reads-in the input strings

# for _ in range(n):                # original input function
#     matrix_item = input()
#     matrix.append(matrix_item)

for line in txt_input.splitlines():  # modified input function
    matrix.append(line)
sentence = ''
res = []

# rearranges the input strings, connects them to a single long string
for ele in zip(*matrix):
    sentence += ''.join(ele)

# uses regular expression library to find where a non-ASCII char is enclosed by two ASCII chars and replace it with a space char
print(re.sub("(?<=\w)([\W]+)(?=\w)", " ", r'{}'.format(sentence)))
