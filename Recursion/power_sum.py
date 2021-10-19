import math

"""
Find the number of ways that a given integer, , can be expressed as the sum of the  powers of unique, natural numbers.
"""


def power_sum(num, power, x=None):
    if num <= 1:
        return 1
    sum = 0

    if x is None:
        x = math.floor(num ** (1 / power))
    for i in range(x, 0, -1):
        y = i ** power
        dif = num - y
        if dif < 0:
            continue
        elif dif == 0:
            sum += 1
        else:
            if i > 1:
                sum += power_sum(dif, power, i - 1)
    return sum


print(power_sum(800, 2))
# print(power_sum(800, 2)) = 561
# print(power_sum(30, 2))
