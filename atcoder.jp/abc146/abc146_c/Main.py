def money(a,b,n):
  cnt=0
  N=n
  while n!=0:
    n//=10
    cnt+=1
  return (a*N+b*cnt)

a,b,x=map(int,input().split())
start=1
goal=10**9+1
ans=0
while start<goal:
  half=(start+goal)//2
  if money(a,b,half)>x:
    goal=half
  else:
    start=half+1
    ans=max(ans,half)

print(ans)