n, d = map(int, input().split())
t = list(map(int, input().split()))

for st, en in zip(t[:-1], t[1:]):
  if en - st <= d:
    print(en)
    exit()
print(-1)
