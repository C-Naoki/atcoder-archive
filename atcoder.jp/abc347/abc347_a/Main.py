n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = list()
for i in range(n):
  if A[i] % k == 0:
    ans.append(str(A[i] // k))

print(' '.join(ans))
