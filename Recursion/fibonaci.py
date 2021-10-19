# recursion - naive
def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# with memoization
memo = {}


def fib_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        f = 0
    elif n <= 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f


# Bottom up
fib_dic = {}
n = 38
for k in range(n + 1):
    if k <= 2:
        f = 1
    else:
        f = fib_dic[k - 1] + fib_dic[k - 2]
    fib_dic[k] = f
print(fib_dic[n])

# Call
print(fib(38))
print(fib_memo(38))
