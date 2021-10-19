import numpy as np


def rotate_matrix(my_array):
    my_list = list(zip(*my_array))
    new_list = []
    for i in my_list:
        j = list(i)
        j.reverse()
        new_list.append(j)
    return np.array(new_list)


my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
a1 = rotate_matrix(my_array)
print(a1)
a2 = rotate_matrix(a1)
print(a2)
a3 = rotate_matrix(a2)
print(a3)
a4 = rotate_matrix(a3)
print(a4)
