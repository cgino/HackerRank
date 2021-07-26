# Given an array of integers, determine whether the array is monotonic or not.

import numpy as np

A = [6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]

# def monoton_check(arr):
#     increase = all(arr[1:] - arr[:-1] >= 0)
#     decrease = all(arr[1:] - arr[:-1] <= 0)
#     return increase or decrease


def monoton_check(arr):
    return all(arr[1:] - arr[:-1] >= 0) or all(arr[1:] - arr[:-1] <= 0)

print(monoton_check(np.array(C)))

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4,4,5,6,7,8,1,0,0,1,2,2,3,4,6, 0, 0]
print(len(array2))

def solution(nums):
    j = 0
    for x, i in enumerate(nums):

        if i == 0:
            j += 1
            nums.remove(0)
            nums.append(0)
            print('j:', j)
        print(nums)
        if len(nums) - j + 1 < x:  break
    return nums

print('sol:', solution(array2))
