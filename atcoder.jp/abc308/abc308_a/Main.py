s = list(map(int, input().split()))
for s_b, s_a in zip(s[:-1], s[1:]):
  if s_b > s_a:
    print("No")
    exit()
for s_i in s:
  if s_i < 100 or s_i > 675 or s_i % 25 != 0:
    print("No")
    exit()
print("Yes")