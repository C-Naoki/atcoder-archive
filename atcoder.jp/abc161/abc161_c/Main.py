N,K = map(int,input().split())

j = N//K

if N-j*K > -(N-(j+1)*K):
    print(-(N-(j+1)*K))
else:
    print(N-j*K)