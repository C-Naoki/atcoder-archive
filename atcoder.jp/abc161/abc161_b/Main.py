N,M = map(int,input().split())
A = list(map(int,input().split()))

total=0
for i in range(N):
    total+=A[i]

count=0
for i in range(N):
    if A[i]*4*M>=total:
        count+=1

if count>=M:
    print('Yes')
else:
    print('No')