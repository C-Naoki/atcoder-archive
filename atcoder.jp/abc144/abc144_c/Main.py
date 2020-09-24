n = int(input())
m = int(n ** 0.5 + 1)
for i in range(m,0,-1):
    if n % i == 0:
        print((i - 1) + ((n // i) - 1))
        exit()