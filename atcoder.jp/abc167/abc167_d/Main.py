'''
path = 'sub1_51.txt'
f=open(path)
data1 = f.read()
f.close()
N=data1.split()
'''
n,k=map(int,input().split())
A=list(map(int,input().split()))
'''
n=int(N[0])
k=int(N[1])
A=N[2:]
'''
A=[int(i)-1 for i in A]
B=[]
cnt=[0]*n
m=0
for i in range(2*10**5):
    B.append(m)
    cnt[m]+=1
    if cnt[m]>1:
        break
    m=A[m]
c=len(B)-(B.index(m)+1)
print(1+B[(max(k-B.index(m),0))%c + min(B.index(m),k)])
#Bは街の移動順序
#cはループの長さ