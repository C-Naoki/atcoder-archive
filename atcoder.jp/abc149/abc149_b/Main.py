a, b, k = map(int,input().split())
if a + b < k:
    a = 0
    b = 0
elif a < k:
    b = b + a - k
    a = 0
else:
    a = a - k

print(a,b)