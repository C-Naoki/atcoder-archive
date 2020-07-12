def prime_factorize(n):
    ans = []
    while n % 2 == 0:
        ans.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ans.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        ans.append(n)
    return ans

a,b = map(int,input().split())
A = prime_factorize(a)
B = prime_factorize(b)
G = []
for i in set(A):
    if i in set(B):
        G.append(i)
print(len(set(G)) + 1)