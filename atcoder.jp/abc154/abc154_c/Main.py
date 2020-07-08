n=input()
A=list(map(int,input().split()))
B=set(A)
if len(A)==len(B):
    print('YES')
else:
    print('NO')