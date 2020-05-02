N = int(input())
S = [i for i in input()]

r = 0
g = 0
b = 0
no = 0

for i in S:
    if i == "R":
        r += 1
    elif i == "G":
        g += 1
    else:
        b += 1

for i in range(N):
    for j in range(i+1, N):
        k = j*2 - i
        if k >= N:
            break
        elif S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            no += 1
 
print(r*g*b - no)