# n(n+1)/2


def missing_number(my_list, n):
    total_sum = (n * (n + 1)) / 2
    list_sum = sum(my_list)
    print(total_sum - list_sum)


my_list = [1, 2, 3, 4, 5, 6, 7, 9]
missing_number(my_list, 9)
