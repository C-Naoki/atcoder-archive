a,b,n = map(int, input().split())
m = min(n,b-1)
print(int(a*m/b)-a*int(m/b))