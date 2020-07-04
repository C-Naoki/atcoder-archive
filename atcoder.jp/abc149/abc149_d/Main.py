n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
total=0
M=[0]*n
for i in range(n):
  if t[i]=='r' and (i<k or M[i-k]!='p'):
    M[i]='p'
    total+=p
  elif t[i]=='s' and (i<k or M[i-k]!='r'):
    M[i]='r'
    total+=r
  elif t[i]=='p' and (i<k or M[i-k]!='s'):
    M[i]='s'
    total+=s
  #print(total,t[i-k],t[i],i-k)
print(total)