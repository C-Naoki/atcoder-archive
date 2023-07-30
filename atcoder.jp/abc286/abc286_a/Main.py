N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

P -= 1
Q -= 1
R -= 1
S -= 1

B = A[:P] + A[R:S+1] + A[Q+1:R] + A[P:Q+1] + A[S+1:]

print(" ".join(map(str, B)))
