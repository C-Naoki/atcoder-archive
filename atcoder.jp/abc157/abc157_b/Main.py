f = lambda:list(map(int,input().split()))
l = f() + f() + f()
n = int(input())
s = set()

for i in range(n):
    b = int(input())
    if b in l: s|={l.index(b)}

print(['No','Yes'][any(t<=s for t in [{0,1,2},{0,3,6},{0,4,8},{1,4,7},
                                      {2,4,6},{2,5,8},{3,4,5},{6,7,8}])])