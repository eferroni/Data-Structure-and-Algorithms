import numpy as np


def linear_search(myArray, number):
    for i in range(len(myArray)):
        if myArray[i] == number:
            print(i)


myArray = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
)
linear_search(myArray, 13)
