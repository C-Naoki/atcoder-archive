n, a, x, y = map(int, input().split())

print(min(a, n) * x + max((n - a), 0) * y)
