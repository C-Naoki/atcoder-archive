n = int(input())
w = list(map(str, input().split()))

target = ["and", "not", "that", "the", "you"]

ans = "No"
for w_i in w:
  if w_i in target:
    ans = "Yes"
print(ans)
