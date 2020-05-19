s = str(input())
kekka = 1
for i in range(len(s)):
  if i%2 == 0 and s[i] != 'h':
    kekka = -1
    break
  elif i%2 == 1 and s[i] != 'i':
    kekka = -1
    break
if kekka == 1 and len(s)%2 == 0:
  print('Yes')
else:
  print('No')