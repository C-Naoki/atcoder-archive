import math
a,b,c,d=map(int,input().split())

l1 = a % c
r1 = b % c

if l1 > r1:
    cnt1 = (b - a)//c + 1
else:
    cnt1 = (b - a)//c
if l1 == 0:
    cnt1 += 1

l2 = a % d
r2 = b % d

if l2 > r2:
    cnt2 = (b - a)//d + 1
else:
    cnt2 = (b - a)//d
if l2 == 0:
    cnt2 += 1

e = (c*d)//math.gcd(c,d)
l3 = a % e
r3 = b % e

if l3 > r3:
    cnt3 = (b - a)//e + 1
else:
    cnt3 = (b - a)//e
if l3 == 0:
    cnt3 += 1

print((b - a + 1) - cnt1 - cnt2 + cnt3)