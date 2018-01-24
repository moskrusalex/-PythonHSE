def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def cnk(n, k):
    return fact(n) // (fact(k) * fact(n - k))


def alt_cnk(n, k):
    if n == k or k == 0:
        return 1
    return cnk(n - 1, k) + cnk(n - 1, k - 1)


n = int(input())
k = int(input())
print(alt_cnk(n, k))
