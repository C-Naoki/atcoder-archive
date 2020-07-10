n,k=map(int,input().split())
H=list(map(int,input().split()))
dp=[0]*n
for i in range(1,n):
    S=[]
    for j in range(1,min(k+1,i+1)):
        S.append(dp[i-j]+abs(H[i]-H[i-j]))
    dp[i]=min(S)
print(dp[n-1])