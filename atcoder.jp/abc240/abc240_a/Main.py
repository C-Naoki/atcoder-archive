a, b = map(int, input().split())

if max(a, b) - min(a, b) == 1 or max(a, b) - min(a, b) == 9:
  print("Yes")
else:
  print("No")
