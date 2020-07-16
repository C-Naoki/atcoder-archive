n, k = map(int,input().split())
A = list(map(int,input().split()))

right = 0
ans = 0
total = 0
for left in range(0,n):
    if left != 0:
        total -= A[left - 1]
    while total + A[right] < k:
        total += A[right]
        right += 1
        #print(left,right,total,k)
        if right == n:
            print(ans)
            exit()
    ans += n - right
print(ans)