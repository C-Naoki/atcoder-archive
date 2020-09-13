n = int(input())
M = 10 ** n
m1 = 8 ** n
m2 = (9 ** n) - (8 ** n) 

print((M - m1 - 2*m2)%((10 ** 9) + 7))