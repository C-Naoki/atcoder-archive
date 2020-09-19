n = int(input())
ans = 0
last = 0
for i in range(n):
  d1, d2 = map(int,input().split())
  if d1 == d2:
    ans += 1
  else:
    last = max(last,ans)
    ans = 0
last = max(last,ans)
if last > 2:
  print('Yes')
else:
  print('No')
