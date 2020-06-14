x,n=map(int,input().split())
P=list(map(int,input().split()))
Q=P.copy()

for i in range(n):
    P[i]=abs(P[i]-x)
P.sort()
count = -1
for i in range(n):
    if (i+1)//2 == P[i]:
        continue
    else:
        count=(i+1)//2
        break

if n%2==0 and count==-1:
    count=n//2
elif n%2==1 and count==-1:
    count=(n+1)//2

if n==0:
    print(x)
elif x-count in Q:
    print(x+count)
else:
    print(x-count)