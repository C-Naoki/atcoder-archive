h,w,k=map(int,input().split())
s=[]
Sh=[0]*h
Sw=[0]*w
cnt=[]
Th=[]
Tw=[]
for i in range(h):
    s.append(input())

for i in range(h):
    cnt.append(s[i].count('#'))

for i in range(w):
    c=0
    for j in range(h):
        if s[j][i]=='#':
            c+=1
    cnt.append(c)
#cntの1~hは　行　の#の個数。h+1~wは　列　の#の個数

#関数の定義
def cheak(s,i,j):
    if s[i][j]=='#':
        return 1
    else:
        return 0

def rech(k):
    totalh=0
    if k==h:
        for i in range(h):
            if Sh[i]==1:
                totalh+=cnt[i]
        #print(Sh, totalh)
        th=Sh.copy()
        Th.append(th)
        Th.append(totalh)
        return
    rech(k+1)
    Sh[k]=1
    rech(k+1)
    Sh[k]=0

def recw(k):
    totalw=0
    if k==w:
        for i in range(w):
            if Sw[i]==1:
                totalw+=cnt[h+i]
        #print(Sw, totalw)
        tw=Sw.copy()
        Tw.append(tw)
        Tw.append(totalw)
        return
    recw(k+1)
    Sw[k]=1
    recw(k+1)
    Sw[k]=0

total=sum(cnt[0:h])
ans=0
'''
for i in range(h):
    for j in range(w):
        if total-(cnt[i]+cnt[h+j]-cheak(s,i,j))==k:
            ans+=1
'''
rech(0)
recw(0)
#print(Th)
#print(Tw)

for i in range(2**h):
    for j in range(2**w):
        cheaktotal=0
        for p in range(h):
            for q in range(w):
                if Th[2*i][p]==1 and Tw[2*j][q]==1:
                    cheaktotal+=cheak(s,p,q)
        if total-Th[2*i+1]-Tw[2*j+1]+cheaktotal==k:
            ans+=1
print(ans)
