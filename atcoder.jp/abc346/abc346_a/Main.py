n = int(input())
A = list(map(int, input().split()))

B = list()
for i in range(n - 1):
  B.append(str(A[i + 1] * A[i]))

print(' '.join(B))
