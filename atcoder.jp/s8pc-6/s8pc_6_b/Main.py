n = int(input())
AB = list()
ans = 10 ** 20
for i in range(n):
    A, B = map(int, input().split())
    AB.append([A, B])
for i in range(n):
    for j in range(n):
        enter = AB[i][0]
        exit = AB[j][1]
        total = 0
        for k in range(n):
            total += abs(enter - AB[k][0]) + abs(AB[k][1] - AB[k][0]) + abs(exit - AB[k][1])
        ans = min(ans, total)
print(ans)