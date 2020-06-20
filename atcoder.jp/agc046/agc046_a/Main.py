x=int(input())
a=x
k=0
while x!=0:
  x+=a
  x%=360
  k+=1
print(k+1)