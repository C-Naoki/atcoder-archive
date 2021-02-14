n, m = map(int, input().split())
A = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
ans = 0
for song1 in range(m):
    for song2 in range(song1 + 1, m):
        point = 0
        for person in range(n):
            point += max(A[person][song1], A[person][song2])
        ans = max(ans, point)
print(ans)