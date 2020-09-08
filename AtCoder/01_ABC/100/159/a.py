import math

N, M = map(int, input().split())

def combinations_count(n, r):
    if n >= r :
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    else :
        return 0

print(combinations_count(N, 2) + combinations_count(M, 2))