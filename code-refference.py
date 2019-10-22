# 二分探索
from bisect import bisect_left

# a, b にユークリッドの互除法を使い、a を最大公約数にする
while b:
    a, b = b, a % b

# 素因数分解
def factorization(a):
    arr = []
    temp = a
    for i in range(2, int(-(-a**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([a, 1])

    return arr