n = int(input())
A=[0]*n
B=[0]*(n-1)
for i in range(n):
    A[i]=int(input())
    if i==0:
        continue
    elif A[i-1]<A[i]:
        B[i-1]='up'
    elif A[i-1]>A[i]:
        B[i-1]='down'
    else:
        B[i-1]='stay'

for i in range(n-1):
    if B[i]=='up':
        print('up',A[i+1]-A[i])
    elif B[i]=='down':
        print('down',A[i]-A[i+1])
    else:
        print('stay')