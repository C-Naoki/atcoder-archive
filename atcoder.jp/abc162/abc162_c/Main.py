from math import gcd
k = int(input()) + 1
total = 0

for i in range(1,k):
    for j in range(1,k):
        for l in range(1,k):
            total += gcd(gcd(i,j),l)

print(total)