def permutation(list1, list2):
    if list1.sort() == list2.sort():
        print("yes")
    else:
        print("no")


list1 = [4, 3, 2, 1]
list2 = [1, 2, 3, 4]
permutation(list1, list2)
