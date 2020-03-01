n, m = map(int, input().split())

listans = [0] * n
ans = 0

for i in range(m):
    s, c = map(int, input().split())
    s -= 1
    if listans[s] == 0:
        listans[s] = c
    elif listans[s] != c:
        ans = -1
    if n > 1 and s == 0 and c == 0:
        ans = -1

if n > 1 and listans[0] == 0:
    listans[0] = 1

if ans == 0:
    ans = "".join([str(li) for li in listans])

print(ans)