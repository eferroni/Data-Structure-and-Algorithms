"""
How to find GCD (Greater Common Divisor) of two numbers using recursion?
Based on Euclidean Algorithm
"""


def GCD(n1, n2):
    assert n1 != 0 and n2 != 0 and int(n1) == n1 and int(n2) == n2, "error"
    if n1 < 0:
        n1 *= -1
    if n2 < 0:
        n2 *= -1
    if n1 % n2 == 0:
        return n2
    return GCD(n2, n1 % n2)


def GCD2(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        return GCD2(n1 - n2, n2)
    else:
        return GCD2(n1, n2 - n1)


print(GCD(48, 18))
print(GCD2(48, 18))
