n = int(input())
A = list(map(int,input().split()))
B = A.copy()
ans = 0
for i in range(n-1):
    if A[i+1] < A[i]:
        A[i+1] += (A[i] - A[i+1])
        ans += (A[i+1] - B[i+1])
print(ans)