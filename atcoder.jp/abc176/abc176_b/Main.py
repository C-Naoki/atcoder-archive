n = input()
N = [0]*len(n)
for i in range(len(n)):
    N[i] = int(n[i])
if (sum(N) % 9) == 0:
    print('Yes')
else:
    print('No')