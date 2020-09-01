n = int(input())
A = list(map(int,input().split()))
ans = [0]*n
for i in range(n):
    ans[A[i] - 1] = str(i + 1)

Ans = ' '.join(ans)
print(Ans)