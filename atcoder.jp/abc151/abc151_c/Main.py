n,m=map(int,input().split())
cnt = [0]*n
total = [0]*n
for i in range(m):
    P=list(input().split())
    p = int(P[0]) - 1
    if P[1] == 'WA' and cnt[p] == 0:
        total[p] += 1
    if P[1] == 'AC' and cnt[p] == 0:
        cnt[p] = True
ans = 0
for i in range(n):
    if cnt[i] == True:
        ans += total[i]
print(sum(cnt),ans)