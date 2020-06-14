x,y=map(int,input().split())
if y%2!=0:
    print('No')
elif (y-2*x)//2 < 0 or (4*x-y)//2 < 0:
    print('No')
elif (y-2*x)//2 == 0 and (4*x-y)//2==0:
    print('No')
else:
    print('Yes')