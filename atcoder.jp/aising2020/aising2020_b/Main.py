n=int(input())
A=list(map(int,input().split()))
cnt=0
for i in range(n):
    if i%2==0 and A[i]%2==1:
        cnt+=1
print(cnt)