def check(learn_total):
    for i in range(m):
        if learn_total[i] < x:
            return False  
    return True 

def calc_price(bit):
    price_total = 0 
    learn_total = [0] * m 

    for i in range(n):
        if (bit >> i) & 1:  
            price_total += c[i]  
            learn = a[i]  
            for j, la in enumerate(learn): 
                learn_total[j] += la

   
    if check(learn_total):
        return price_total 
    else:
        return INF

if __name__ == '__main__':
    n, m, x = list(map(int, input().split()))

    # 空のリストを作って、appendで追加していきます
    c = []  # 参考書の値段です
    a = []  # 各参考書に入る理解度です

    for i in range(n):
        c_temp, *a_temp = list(map(int, input().split()))  # こうすると、2つ目以降をリストで受け取れます
        c.append(c_temp)
        a.append(a_temp)

    INF = float("inf")
    ans = INF

    for bit in range(1 << n):
        price = calc_price(bit)  # 条件を満たすならそのときの値段、満たさないならINFが返ってきます
        ans = min(ans, price)  # 答えを更新します

    if ans == INF:
        print(-1)  # どうやっても条件を満たせなかった
    else:
        print(ans) 