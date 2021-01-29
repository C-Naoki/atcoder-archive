n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(i):
        for k in range(j):
            x1, y1 = p[i]
            x2, y2 = p[j]
            x3, y3 = p[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 == x2 * y1:
                print("Yes")
                exit()

print("No")