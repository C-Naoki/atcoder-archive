n, k, a = map(int, input().split())

print(n if (a + k - 1) % n == 0 else (a + k - 1) % n)
