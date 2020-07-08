n=int(input())
P=list(map(int,input().split()))
m = n + 1
cnt = 0
for i in range(n):
    if m >= P[i]:
        m = P[i]
        cnt += 1
print(cnt)