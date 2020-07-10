n=int(input())
H=list(map(int,input().split()))
dp=[0]*n
dp[1]=abs(H[1]-H[0])
for i in range(n-2):
    dp[i+2]=min(dp[i]+abs(H[i+2]-H[i]),dp[i+1]+abs(H[i+2]-H[i+1]))
print(dp[n-1])