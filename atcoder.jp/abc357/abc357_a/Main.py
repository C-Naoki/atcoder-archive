n, m = map(int, input().split())
h = list(map(int, input().split()))

cnt = 0
for i in range(len(h)):
  if m - h[i] < 0:
    print(cnt)
    exit()
  m -= h[i]
  cnt += 1

print(n)
