x, y, n = map(int, input().split())

if y < 3 * x:
  n_y = n // 3
  n_x = n % 3
  print(x * n_x + y * n_y)
else:
  print(n * x)
