n=int(input())
L=list(map(int,input().split()))
L.sort(reverse = True)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        cnt = 0
        start=j+1
        goal=n
        while goal!=start:
            half = (start + goal)//2
            if L[i] < L[j] + L[half]:
                start = half + 1
                cnt = max(half-j,cnt)
            else:
                goal = half
        ans += cnt
print(ans)