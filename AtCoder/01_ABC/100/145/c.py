n = int(input())

towns = []
count = 0
lenSum = 0

for i in range(n) :
    tmp = list(map(int, input().split()))
    towns.append(tmp)

for p in range(len(towns)-1) :
    for q in range(p+1, len(towns)) :
        lenSum += ((towns[p][0] - towns[q][0]) ** 2 + (towns[p][1] - towns[q][1]) ** 2) ** 0.5
        count += 1

print(lenSum / count * (n - 1))