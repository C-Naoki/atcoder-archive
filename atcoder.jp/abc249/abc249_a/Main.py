a, b, c, d, e, f, x = map(int, input().split())

takahashi = 0
aoki = 0
flag_t = [1] * a + [0] * c
flag_a = [1] * d + [0] * f
for i in range(x):
  if flag_t[i % (a + c)]:
    takahashi += b
  if flag_a[i % (d + f)]:
    aoki += e

if takahashi > aoki:
  print("Takahashi")
elif takahashi < aoki:
  print("Aoki")
else:
  print("Draw")
