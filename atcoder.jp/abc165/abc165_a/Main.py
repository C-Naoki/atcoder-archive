k = int(input())
a,b = map(int,input().split())
kekka = 0

for i in range(a,b+1):
    if i%k == 0:
        kekka = 1
        break

if kekka == 1:
    print("OK")
else:
    print("NG")