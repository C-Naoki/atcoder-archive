M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
  m += 1
  d = 0
  if m - 1 == M:
    y += 1
    m = 1
print(y, m, d + 1)
