n, x = map(int, input().split())

block_size = 26 * n

repeat_num = (x - 1) // block_size

remainder = (x - 1) % block_size

alphabet_idx = remainder // n

answer = chr(ord('A') + alphabet_idx)

print(answer)
