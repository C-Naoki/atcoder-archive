s = str(input())
kekka = 1
n = len(s)
if s != s[::-1]:
    kekka = -1
if s[:(n-1)//2] != s[(n-3)//2::-1]:
    kekka = -1
if s[(n+1)//2:] != s[n-1:(n-1)//2:-1]:
    kekka = -1
if kekka == 1:
    print('Yes')
else:
    print('No')