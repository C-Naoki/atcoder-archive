N, L, R = map(int, input().split())

A = list(range(1, N + 1))

A[L-1:R] = reversed(A[L-1:R])

print(" ".join(map(str, A)))
