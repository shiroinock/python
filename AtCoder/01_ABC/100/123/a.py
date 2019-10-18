n = []

for i in range(0,5) :
    n.append(int(input()))

k = int(input())

count = 0

for p in range(0, 4) :
    for q in range(p + 1, 5) :
        if n[q] - n[p] > k :
            print(':(')
            exit()

print('Yay!')