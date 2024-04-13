def euclid_distance(x1, y1, x2, y2):
  return (x1 - x2) ** 2 + (y1 - y2) ** 2


n = int(input())

X, Y = list(), list()
for _ in range(n):
  x, y = map(int, input().split())
  X.append(x), Y.append(y)

for i in range(n):
  ans = -1
  ans_idx = 0
  for j in range(n):
    if i != j:
      ij_dist = euclid_distance(X[i], Y[i], X[j], Y[j])
      if ij_dist > ans:
        ans = ij_dist
        ans_idx = j + 1
  print(ans_idx)
