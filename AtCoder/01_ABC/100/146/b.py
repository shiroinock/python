alps = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

n = int(input())
s = input()

ans = ''

for i in range(len(s)) :
    idx = (alps.index(s[i]) + n) % 26
    ans += alps[idx]

print(ans)