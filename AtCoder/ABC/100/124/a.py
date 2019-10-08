n = list(map(int, input().split()))

n.sort()
coin = 0

for i in range(0, 2) :
    coin += n[1]
    n[1] -= 1
    n.sort()

print(coin)