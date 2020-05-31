import math
import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n = int(input())
N = collections.Counter(prime_factorize(n))
total = 0
for i in N.values():
    for j in range(40):
        if j*(j+1)//2 <= i < (j+1)*(j+2)//2:
            total += j
            break
print(total)