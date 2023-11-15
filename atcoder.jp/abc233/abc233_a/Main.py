x, y = map(int, input().split())

print(max(0, int((y - x - 0.1) // 10 + 1)))
