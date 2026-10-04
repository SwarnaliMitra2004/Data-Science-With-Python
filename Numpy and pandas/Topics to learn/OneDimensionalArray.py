import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)

reshaped_arr = arr.reshape(2, 3)

print("Reshaped array:")
print(reshaped_arr)