N,M=map(int,input().split())
A=list(map(int,input().split()))
i = 0
total = 0
while i<M:
    total += A[i]
    i+=1
if N<total:
    print("-1")
else:
    print(N-total)