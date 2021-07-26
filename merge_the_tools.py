# https://www.hackerrank.com/challenges/merge-the-tools/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

# A string, s, of length n where s=c_0c_1...c_n-1.
# An integer,k, where k is a factor of n.
# We can split s into n/k substrings where each subtring, t_i, consists of a contiguous block of k characters in s.
# Then, use each t_i to create string u_i such that: The characters in u_i are a subsequence of the characters in t_i.
# Any repeat occurrence of a character is removed from the string such that each character in u_i
# occurs exactly once. In other words, if the character at some index j in t_i occurs at a previous index < j in t_i,
# then do not include the character in string u_i.
# Given s and k, print n/k lines where each line i denotes string u_i.

# Example:
#
# Sample input:                               Sample Output:
# s = 'AAABCCADDE'                            'AB'
# k = 3                                       'CA'
#                                             'AD'
#

def gen(string, k):
    for i in range(len(string)//k):
        substring = string[i*k: (i+1)*k]
        remains = ''
        for s in substring:
            if s not in remains:
                remains += s

        yield remains

def merge_the_tools(string, k):

    for i in gen(string, k):
        print(i)


if __name__ == '__main__':
    '''Code could solve all test cases, for own input remove comment character below.
    '''
    # string, k = input('string input'), int(input('int input'))
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
