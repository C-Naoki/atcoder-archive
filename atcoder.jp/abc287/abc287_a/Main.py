N = int(input())
votes = [input() for _ in range(N)]
print("Yes" if votes.count("For") > N // 2 else "No")
