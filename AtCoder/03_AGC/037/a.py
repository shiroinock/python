S = str(input())

tmp= S[0]
now = ""
count = 1

for i in range(1, len(S)):
    now += S[i]
    if tmp != now:
        tmp = now
        now = ""
        count += 1

print(count)