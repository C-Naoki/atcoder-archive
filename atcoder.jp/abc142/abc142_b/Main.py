n, k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(n):
  if A[i] >= k:
    ans += 1
print(ans)