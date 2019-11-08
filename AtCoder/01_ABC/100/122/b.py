acgt = ['A', 'C', 'G', 'T']

s = list(input())

tmp = 0
ans = 0

for i in range(len(s)) :
    if acgt.count(s[i]) == 1 :
        tmp += 1
    else :
        tmp = 0
    
    if tmp > ans :
        ans = tmp

print(ans)