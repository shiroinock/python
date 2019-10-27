n = int(input())

w = list(map(int, input().split()))

sum_l = 0
sum_r = 0
l = 0
r = len(w) - 1

for i in range(len(w)) :
    if sum_l <= sum_r :
        sum_l += w[l]
        l += 1
    else :
        sum_r += w[r]
        r -= 1

print(abs(sum_l - sum_r))