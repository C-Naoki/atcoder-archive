H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

min_i = min_j = float('inf')
max_i = max_j = -1

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if S[i][j] == ".":
            print(i + 1, j + 1)