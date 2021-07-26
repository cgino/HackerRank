# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
import numpy as np

str1 = 'aaaaaaaaaaaaaaaggggggggggdddddk'
str2 = 'zasdasdfasdferjalöknvkjböoiuh4uib5jb5iu ' \
       'fjasdfze'


def unique_char(word):
    # non_unique = set()
    # uniquness = np.ones((len(word), 1))
    # for i in range(len(word)):
    #     if not non_unique.intersection(word[i]):
    #         non_unique = non_unique.union(word[i])
    #     else:
    #         uniquness[i] = 0
    #     print(uniquness)
    #     print(non_unique)

    char_dict = {}
    print(type(char_dict))
    print(char_dict)
    # print(char_dict['asdf'])
    for ch in word:
        if ch in char_dict:
            char_dict[ch] = char_dict.get(ch) + 1
        else:
            char_dict[ch] = 1

    print(char_dict)
    for ch, num_appearance in char_dict.items():
        if num_appearance == 1:
            first_unique_char = ch

            return first_unique_char, word.find(ch)
    return -1

# def solution(s):
#     frequency = {}
#     for i in s:
#         if i not in frequency:
#             frequency[i] = 1
#         else:
#             frequency[i] +=1
#     print(frequency)
#     for i in range(len(s)):
#         if frequency[s[i]] == 1:
#             return i
#     return -1



if __name__ == '__main__':
    # input_string = input("Enter string:")
    print(unique_char(str2))
    # print(solution('alphabet'))