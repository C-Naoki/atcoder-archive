N,M = map(int,input().split())
i = 0
l = [-1]*N
t = 0
while i<M:
    s,c = map(int,input().split())
    if N>1 and s == 1 and c == 0:
        t = -1
    elif l[s-1] == -1 or l[s-1] == c:
        l[s-1] = c  
    else:
        t = -1 
    i+=1

if N>1 and l[0] == -1:
    l[0] = 1
elif l[0] == -1:
    l[0] = 0

for i in range(0,N):
    if l[i]==-1:
        l[i]=0
    i+=1

if t == 0:
    for i in range(0,N):
        t += l[i]*(10**(N-i-1))
        i+=1

print(t)