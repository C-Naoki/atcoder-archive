x = [0] * 3
y = [0] * 3
for i in range(3):
  x[i], y[i] = map(int, input().split())

x_ans = [xi for xi in x if x.count(xi) == 1][0]
y_ans = [yi for yi in y if y.count(yi) == 1][0]

print(x_ans, y_ans)
