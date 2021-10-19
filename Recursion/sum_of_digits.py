"""
How to find the sum of digits of a positive integer number using recursion?
"""


def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "n is lower than 0 or not a int"
    if n < 10:
        return n

    return sum_of_digits(n // 10) + n % 10


print(sum_of_digits(0.6))
