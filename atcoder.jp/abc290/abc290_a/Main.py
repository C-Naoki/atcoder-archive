n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0
for b_i in b:
  total += a[b_i - 1]
print(total)
