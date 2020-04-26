a,b,c,d = map(int,input().split())
count1 = 0
count2 = 0

while c>0:
    c=c-b
    count1+=1

while  a>0:
    a=a-d
    count2+=1

if count1>count2:
    print('No')
else:
    print('Yes')