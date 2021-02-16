from copy import deepcopy

r, c = map(int, input().split())
senbei = list()
ans = 0
for i in range(r):
    row = list(map(int, input().split()))
    senbei.append(row)
for i in range(2 ** (r-1)):
    total = 0
    temp = list(format(i, '010b'))
    #print(temp)
    senbei2 = deepcopy(senbei)
    total = 0
    for j in range(c):
        one = 0
        zero = 0
        column = [x[j] for x in senbei2]
        for k in range(r):
            if column[k] ^ int(temp[10 - r + k]):
                one += 1
            else:
                zero += 1
        total += max(zero, one)
    ans = max(ans, total)
    #print(total, temp)
print(ans)