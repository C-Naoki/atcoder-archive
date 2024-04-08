A =list(map(int, input().split()))

A.sort()
print("Yes" if A[2] - A[1] == A[1] - A[0] else "No")
