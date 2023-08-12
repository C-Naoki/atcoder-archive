S = input().strip()

position = S.rfind('a')

print(position + 1 if position != -1 else -1)
