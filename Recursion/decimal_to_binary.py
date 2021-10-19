import sys

"""
How to convert a number from Decimal to Binary using recursion?
"""


def decimal_to_binary(n):
    assert n >= 0 and int(n) == n, "error"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return decimal_to_binary(n // 2) * 10 + n % 2


print(decimal_to_binary(13))
print(decimal_to_binary(10))
