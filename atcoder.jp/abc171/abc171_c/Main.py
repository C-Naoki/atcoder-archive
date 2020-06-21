n=int(input())
m=n
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(1,12):
  n-=26**i
  if n<=0:
    count=i
    break
n=m

for i in range(1,count):
  n-=26**i
n-=1

B=[]
for i in range(count-1,0,-1):
  B.append(n//(26**i))
  n-=(n//(26**i))*(26**i)
B.append(n)

C=[]
for i in B:
  C.append(A[i])
print(''.join(C))