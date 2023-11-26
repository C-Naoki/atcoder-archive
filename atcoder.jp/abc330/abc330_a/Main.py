n, l = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
  cnt += (A[i] >= l)

print(cnt)
