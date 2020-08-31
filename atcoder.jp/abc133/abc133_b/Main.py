n, d = map(int,input().split())

total = []
for i in range(n):
    x = list(map(int,input().split()))
    total.append(x)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        temp = 0
        for y,z in zip(range(d),range(d)):
            temp += (total[i][y] - total[j][z])**2
        if temp**0.5 == int(temp**0.5):
            ans += 1

print(ans)