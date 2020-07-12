n = int(input())
dic = {}
for i in range(n):
    s = sorted(input())
    try:
        dic[''.join(s)] += 1
    except:
        dic[''.join(s)] = 1
    
ans = 0
for i in dic.values():
    ans += i*(i-1)//2
print(ans)