n = int(input())
A = list(map(int, input().split()))
ans = [0, 0]
for i in range(2, max(A) + 1):
    cnt = 0
    for j in A:
        if j % i == 0:
            cnt += 1
    if ans[0] <= cnt:
        ans[0] = cnt
        ans[1] = i
print(ans[1])