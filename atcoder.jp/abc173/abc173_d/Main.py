n=int(input())
A=list(map(int,input().split()))
A.sort(reverse = True)
total=0
for i in range(n-1):
    total+=A[(i+1)//2]
print(total)