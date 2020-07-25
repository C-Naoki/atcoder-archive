n,k = map(int,input().split())
A = list(map(int,input().split()))
dp=[0]*n
for i in range(n):
    if i < k:
        dp[i] += dp[i-1] + A[i]
    else:
        dp[i] = dp[i-1] + A[i] - A[i-k]
for i in range(k,n):
    if dp[i-1] < dp[i]:
        print('Yes')
    else:
        print('No')