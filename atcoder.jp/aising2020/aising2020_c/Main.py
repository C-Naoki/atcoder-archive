from collections import Counter
n=int(input())
cnt=0
ans=[]
for i in range(2,int((2*n)**0.5)+1):
    for j in range(2,int((2*n)**0.5)+1):
        for k in range(2,int((2*n)**0.5)+1):
            if (i*i + j*j + k*k)%2==0 and (i*i + j*j + k*k)<=2*n and (i+j-k>1) and (i+k-j>1) and (k+j-i>1):
                ans.append((i*i + j*j + k*k)//2)
ans.sort()
A=Counter(ans)
for i in range(1,n+1):
    print(A[i])