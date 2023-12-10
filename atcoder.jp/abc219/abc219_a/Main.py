x = int(input())

thresholds = [40, 70, 90]

for th in thresholds:
  if x < th:
    print(th - x)
    exit()

print("expert")
