import math
a,b,h,m=map(int,input().split())
tyoshin = m*6
tanshin = m*0.5 + h*30
kakudo = abs(tyoshin - tanshin)
print((a*a + b*b -2*a*b*math.cos(kakudo*math.pi/180))**0.5)