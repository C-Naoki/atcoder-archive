a, b = map(int, input().split())

candidate = [1, 2, 3]
candidate.remove(a)
if b not in candidate:
  print(-1)
else:
  candidate.remove(b)
  print(candidate[0])
