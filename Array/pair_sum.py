def pair_sum(my_list, n):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                continue
            elif my_list[i] + my_list[j] == n:
                print(i, j)


my_list = [2, 6, 3, 9, 11]
pair_sum(my_list, 9)
