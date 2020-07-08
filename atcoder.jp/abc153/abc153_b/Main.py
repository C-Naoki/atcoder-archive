h,n=map(int,input().split())
A=list(map(int,input().split()))
attack = sum(A)
if h > attack:
    print('No')
else:
    print('Yes')