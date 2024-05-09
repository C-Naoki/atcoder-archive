n, x, y, z = map(int, input().split())

if min(x, y) <= z <= max(x, y):
  print("Yes")
else:
  print("No")
