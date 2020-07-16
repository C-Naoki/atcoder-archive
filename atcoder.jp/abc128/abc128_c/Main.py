n,m=map(int,input().split())
k = [0]*m
s = [0]*m

for i in range(m):
    k[i], *s[i] = map(int,input().split())

p = list(map(int,input().split()))

ans = 0
for i in range(1 << n):
    cnt = [0]*m
    for j in range(n):
        if (i >> j) % 2 == 1:
            for a in range(m):
                if j + 1 in s[a]:
                    cnt[a] += 1
    chk = 0
    for j in range(m):
        if cnt[j] % 2 != p[j]:
            chk = 1
            break
    if chk == 0:
        ans += 1
print(ans)