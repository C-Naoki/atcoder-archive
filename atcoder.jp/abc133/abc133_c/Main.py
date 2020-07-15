l,r=map(int,input().split())
if r - l >= 2018:
    print(0)
    exit()

m=10000
for i in range(l,r):
    for j in range(i+1,r+1):
        m = min(m,(i*j)%2019)

print(m)