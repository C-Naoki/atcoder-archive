a,b,m = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Min = (min(A)+min(B))
for _ in range(m):
    x,y,c = map(int,input().split())
    if Min > A[x-1]+B[y-1]-c:
        Min=A[x-1]+B[y-1]-c
print(Min)