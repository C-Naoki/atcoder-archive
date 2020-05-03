x = int(input())
A = 0
B = 0
for i in range(-1000,1000):
  if i**5 + x >= 0 and float.is_integer(round((i**5 + x)**0.2,5)) == True:
    A = (i**5 + x)**0.2
    B = i
    break

print(int(A),B)