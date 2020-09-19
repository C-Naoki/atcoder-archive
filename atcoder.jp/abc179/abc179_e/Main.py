n, x, m = map(int,input().split())
rem = [0] * m
chk = [0] * (m + 1)
rem[0] = x
if x == 0:
  print(0)
  exit()

for i in range(1,m):
  rem[i] = (rem[i - 1] ** 2) % m
  if chk[rem[i - 1] ** 2 % m] > 1:
    temp1 = (rem[i - 1] ** 2) % m
    temp2 = i
  else:
    temp1 = (rem[i - 1] ** 2) % m
    temp2 = i

for i in range(m):
  if rem[i] == temp1:
    temp3 = i
    break

if temp2 != temp3:
  num = (n - temp3) // (temp2 - temp3)
  S = sum(rem[:temp3]) + sum(rem[temp3:temp2]) * num + sum(rem[temp3:n - (num * (temp2 - temp3))])
  print(S)
else:
  print(sum(rem))