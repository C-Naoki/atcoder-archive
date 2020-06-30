n,m,k=map(int,input().split())
A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    A[i] += A[i-1]

for i in range(1,m+1):
    B[i] += B[i-1]

ans=0
for a_cnt in range(n+1):
    if A[a_cnt]>k:
        continue
    start=0
    goal=m+1
    while start!=goal:
        b_cnt=(start+goal)//2
        if A[a_cnt]+B[b_cnt]>k:
            goal=b_cnt
        else:
            start=b_cnt+1
            ans=max(ans,a_cnt+b_cnt)
print(ans)
