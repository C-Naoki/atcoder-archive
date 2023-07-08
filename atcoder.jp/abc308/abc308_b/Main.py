n, m = map(int, input().split())
c = list(map(str, input().split()))
d = list(map(str, input().split()))
p = list(map(int, input().split()))

price_map = dict()
for i in range(m + 1):
    if i == 0:
        price_map["other"] = p[i]
    else:
        price_map[d[i - 1]] = p[i]

total = 0
for i in range(n):
    if c[i] not in price_map:
        total += price_map["other"]
    else:
        total += price_map[c[i]]
print(total)
