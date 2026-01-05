import numpy as np

np1 = np.array([1, 2, 3])
print(type(np1))
print(np1.dtype)
print(np1.shape)
print(np1.ndim)
print(np1.size)
print(np1[0])
print(np1[1])
print(np1[2])
print(np1[::-1])
print(np1[::2])
print(np1[::-3])

np11 = np.array([4, 5, 6])
print("concatenated:", np.concatenate((np1, np11)))

np1_reshaped = np1.reshape(3, 1)
print("reshaped np1:\n", np1_reshaped)

print("multiply:", np.multiply(np1, np11))
print("divide:", np.divide(np1, np11))
print("subtract:", np.subtract(np1, np11))
print("add:", np.add(np1, np11))
print("sum of elements (np1 + np11):", np.sum(np1 + np11))
