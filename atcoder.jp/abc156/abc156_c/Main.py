n=int(input())
x=list(map(int,input().split()))
m=10000000000
for p in range(1,100):
    total=0
    for i in range(n):
        total+=(x[i]-p)**2
    if total<m:
        m=total
print(m)