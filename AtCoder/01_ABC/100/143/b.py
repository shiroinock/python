n = int(input())

tako_list = list(map(int, input().split()))
tako_len = len(tako_list)

sum = 0

for i in range(0, n - 1) :
    for j in range(1, tako_len - i) :
        sum += tako_list[i] * tako_list[i + j]

print(sum)
