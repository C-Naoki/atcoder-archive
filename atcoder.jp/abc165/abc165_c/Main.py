from itertools import combinations_with_replacement

n,m,q=map(int,input().split())
A=list(range(1,m+1))
s=(list(combinations_with_replacement(A,n)))
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q

ans=0
for i in range(q):
    a[i],b[i],c[i],d[i]=map(int,input().split())

for i in s:
    total=0
    for j in range(q):
        if i[b[j]-1]-i[a[j]-1]==c[j]:
            total+=d[j]
    ans=max(ans,total)
print(ans)