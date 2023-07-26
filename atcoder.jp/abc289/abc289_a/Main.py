s = input()

result = ""
for char in s:
    if char == '0':
        result += '1'
    else:
        result += '0'

print(result)
