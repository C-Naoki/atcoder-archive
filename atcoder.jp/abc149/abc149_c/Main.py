def prime_num(n):
    f = 3
    while f * f <= n:
        if n % f == 0:
            return 1
        f += 2
    return 0

x = int(input())
if x == 2:
    print(x)
    exit()
prime = (x//2)*2 + 1
while 1 == 1:
    if prime_num(prime) == 0:
        print(prime)
        exit()
    prime += 2