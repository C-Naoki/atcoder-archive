a, b, w = map(int, input().split())
w *= 1000
cnt = 1
ans = list()
while w / cnt >= a:
  _w = w / cnt
  if _w <= b:
    ans.append(cnt)
  cnt += 1

try:
  print(min(ans), max(ans))
except:
  print("UNSATISFIABLE")