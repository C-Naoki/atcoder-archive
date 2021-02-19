t = int(input())
ans = []
for i in range(t):
    l, r = map(int, input().split())
    if r - 2 * l + 1 < 0:
        ans.append(0)
    else:
        ans.append(max(0, (r - 2 * l + 1) * (r - 2 * l + 2) // 2))
for i in ans:
    print(i)