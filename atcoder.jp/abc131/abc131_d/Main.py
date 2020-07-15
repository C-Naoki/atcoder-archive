n = int(input())
A = [0]*n
B = [0]*n
dica = {}
dicb = {}
for i in range(n):
    A[i],B[i] = map(int,input().split())
    dica[i] = A[i]
    dicb[i] = B[i]

dicb = sorted(dicb.items(), key = lambda x:x[1])

time = 0
for i in range(n):
    time += dica[dicb[i][0]]
    if time > dicb[i][1]:
        print('No')
        exit()

print('Yes')