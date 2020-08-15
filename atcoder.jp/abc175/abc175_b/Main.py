n = int(input())
L = list(map(int,input().split()))
L.sort()
ans = 0
n = len(L)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if L[i] + L[j] > L[k] and L[i] < L[j] < L[k]:
                ans += 1
print(ans)