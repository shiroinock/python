

n = int(input())
l = list(map(int, input().split()))

# 多分正解だけど愚直すぎてTLE
l.sort()
count = 0

for i in range(n) :
    for j in range(1, n - i) :
        for k in range(1, n - i - j) :
            if l[i] + l[i + j] >= l[i + j + k] :
                count += 1

print(count)