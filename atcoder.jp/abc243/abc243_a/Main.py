v, a, b, c = map(int, input().split())

v = v % (a + b + c)

if v - a < 0:
  print("F")
elif v - a - b < 0:
  print("M")
else:
  print("T")
