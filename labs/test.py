import numpy as np

print(np.ndarray(5))

print(np.zeros((1, 3)))

a = np.array([i for i in range(20)])

print(a)

b = a.reshape((4, 5)).copy()
print(b)

b[1,3] = 100

print(a)
print(b)

print(np.ones((1,2,3)))

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b, a @ b)

b = np.array([4,5,6,7])

# should show error!!
# print(a + b, a @ b)

print(a.shape, b.shape)

print(np.log(a))
print(np.log(b))
