h, w = map(int, input().split())
r, c = map(int, input().split())

cnt = 0
if r - 1 > 0:
  cnt += 1
if c - 1 > 0:
  cnt += 1
if r + 1 <= h:
  cnt += 1
if c + 1 <= w:
  cnt += 1

print(cnt)
