a,b=map(int,input().split())
if a>b:
  a,b=b,a
L=[str(a)]*b
print(''.join(L))