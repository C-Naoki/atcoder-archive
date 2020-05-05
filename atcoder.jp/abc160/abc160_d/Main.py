n,x,y = map(int,input().split())
A = [0]*n
for i in range(1,n):
    for j in range(i+1,n+1):
        A[min(j-i,abs(i-x)+1+abs(j-y))] += 1

for i in range(1,n):
    print(A[i])