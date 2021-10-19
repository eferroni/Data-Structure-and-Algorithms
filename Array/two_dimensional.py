import numpy as np

my_arr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(my_arr)

# O(n)
# newArray = np.insert(my_arr, 0, [[1, 2, 3, 4]], axis=1)
# print(newArray)

# O(1)
# newArray = np.append(my_arr, [[1, 2, 3, 4]], axis=0)
# print(newArray)
# print("###")
# print(newArray[0][0])

newArray = np.delete(my_arr, 0, axis=1)
print(newArray)
