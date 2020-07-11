n,w=map(int,input().split())
dp = [[0 for i in range(w+1)] for i in range(n+1)]
#print(dp)
for i in range(n):
    weight,value=map(int,input().split())
    for j in range(w+1):
        if j < weight:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j],dp[i][j-weight]+value)
print(dp[n][w])