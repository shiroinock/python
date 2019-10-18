odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']

s = list(input())
ans = 'Yes'

for i in range(len(s)) :
    if i % 2 == 1 and not s[i] in even :
        ans = 'No'
    if i % 2 == 0 and not s[i] in odd :
        ans = 'No'


print(ans)