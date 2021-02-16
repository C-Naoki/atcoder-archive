from collections import Counter
from copy import deepcopy
n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = float('inf')
for i in range(2 ** n):
    Acopy = deepcopy(A)
    temp = list(format(i, '015b'))
    bill = Counter(temp)
    total = 0
    chk = -1
    if bill['1'] != k:
        continue
    for j in range(n):
        if temp[15 - n + j] == '1':
            if j == 0:
                continue
            elif max(Acopy[:j]) >= Acopy[j]:
                total += max(Acopy[:j]) - Acopy[j] + 1
                Acopy[j] = max(Acopy[:j]) + 1
    ans = min(ans, total)
print(ans)