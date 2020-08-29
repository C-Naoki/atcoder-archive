n = int(input())
A = list(map(int,input().split()))
total = sum(A)
ans = 0
for i in range(n):
    total -= A[i]
    ans += A[i]*(total)
print(ans%(10**9 + 7))