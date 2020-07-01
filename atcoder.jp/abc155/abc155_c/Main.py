from collections import Counter
n=int(input())
S=[]
for i in range(n):
    S.append(input())
T=Counter(S)
S=list(set(S))
M=max(T.values())
U=[]
j=0
for i in S:
    if T[i]==M:
        U.append(S[j])
    j+=1
U.sort()
for i in U:
    print(i)