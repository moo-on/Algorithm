#에라토스테네스의 체

n = 1200000000000
a = [False, False] + [True] * (n - 1)
primes = set()
for i in range(2, n + 1):
    if a[i]:
        primes.add(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
