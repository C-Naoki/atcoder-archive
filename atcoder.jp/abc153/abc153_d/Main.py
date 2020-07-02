h=int(input())
cnt=1
while h!=1:
  h//=2
  cnt*=2
print(2*cnt-1)