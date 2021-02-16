import itertools
ans = 0
n, m = map(int, input().split())
xy = set()
for i in range(m):
    x, y = map(int, input().split())
    xy.add((x, y))
for i in range(2 ** n):
    candidates = list()
    for j in range(n):
        if ((i >> j) & 1):
            candidates.append(j + 1)
        chk = 0
        for k in set(itertools.combinations(candidates, 2)):
            if k not in xy:
                chk = 1
        if chk == 0:
            ans = max(ans, len(candidates))
print(ans)