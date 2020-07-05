n=int(input())
i=0
N=n
while n>0:
    n-=1000
    i+=1
print(i*1000-N)