a, b = map(str, input().split())

print(max(sum([int(i) for i in list(a)]), sum([int(i) for i in list(b)])))
