t = str(input())
T = list(t)
for i in range(len(t)):
    if T[i] == '?':
        T[i] = 'D'
print(''.join(T))