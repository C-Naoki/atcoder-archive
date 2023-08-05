H, W = map(int, input().split())
grid = [input() for _ in range(H)]

count = sum(row.count('#') for row in grid)

print(count)
