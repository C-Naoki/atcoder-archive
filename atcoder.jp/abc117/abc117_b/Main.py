n = int(input())
L = list(map(int,input().split()))
kekka = 0
for i in range(n):
  if 2*L[i] >= sum(L):
    kekka = 1
    break
    
if kekka == 1:
  print('No')
else:
  print('Yes')