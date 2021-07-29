import numpy as np


arr = np.arange(12)

arr2 = arr * 3

print(arr, arr2)

logic = arr2 % 2 == 0
print(logic)

arr[logic] = arr2[logic]
print(arr)