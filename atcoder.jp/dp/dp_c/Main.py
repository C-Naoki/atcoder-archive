n=int(input())
dp=[[0 for i in range(3)] for i in range(n)]
dp[0]=list(map(int,input().split()))
for i in range(1,n):
    S=list(map(int,input().split()))
    for j in range(3):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j-2])+S[j]

print(max(dp[n-1]))
#dp[i][j]=i番目にjを選んだ時の最大値(jはa,b,cに対応している。)