n = int(input())
total = 0
for i in range(1,n):
  if n % i == 0:
    chk = (n // i) - 1
  else:
    chk = n // i
  total += chk
print(total)