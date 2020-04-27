n = int(input())
if 0 <= n % 700 < 100:
    print('Yes')
elif  n % 100 > 9 and 0<= (n % 100) % 70 < 10:
    print('Yes')
elif n % 10 == 7:
    print('Yes')
else:
    print('No')