x, y = map(int, input().split("."))

if 0 <= y <= 2:
  print(f"{x}-")
elif 3 <= y <= 6:
  print(x)
else:
  print(f"{x}+")
