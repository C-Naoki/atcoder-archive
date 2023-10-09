n = input()

text = "Yes"

for i in range(len(n) - 1):
    if (n[i] <= n[i+1]):
        text = "No"
        break

print(text)
