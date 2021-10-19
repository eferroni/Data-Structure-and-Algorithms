my_list = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 8, 58, 19, 21]


def unique(my_list):
    new_list = []
    for i in my_list:
        if i in new_list:
            print(i)
        else:
            new_list.append(i)


unique(my_list)
