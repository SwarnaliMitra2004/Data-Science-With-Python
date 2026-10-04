import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)

print("Sliced array:")
print(arr[0:2, 0:2])