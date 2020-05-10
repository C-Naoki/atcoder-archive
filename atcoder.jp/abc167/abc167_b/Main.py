a,b,c,k = map(int,input().split())
M = 0
if a >= k:
    M = k
elif a+b >= k:
    M = a
else:
    M = 2*a - k + b
print(M)