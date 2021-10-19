"""
How to calculate power of a number using recursion?
"""


def power_of_number(n, power):
    assert (
        power >= 0 and int(power) == power
    ), "number and power need to be greater than 0"
    if power == 0:
        return 1
    if power == 1:
        return n
    return n * power_of_number(n, power - 1)


print(power_of_number(1, 10))
