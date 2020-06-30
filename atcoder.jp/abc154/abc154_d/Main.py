n,k=map(int,input().split())
p=list(map(int,input().split()))
for i in range(n):
    p[i]=(p[i]+1)/2
q=[0]*(n-k+1)
q[0]=sum(p[0:k])
for i in range(1,n-k+1):
    q[i]=q[i-1]-p[i-1]+p[k+i-1]
print(max(q))