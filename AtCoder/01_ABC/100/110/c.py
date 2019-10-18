s = input()
t = input()

s_set = list(set(s))
t_set = list(set(t))

s_count = [0] * len(s_set)
t_count = [0] * len(t_set)

for i in range(0,len(s_set)) :
    s_count[i] = s.count(s_set[i])

for j in range(0,len(t_set)) :
    t_count[j] = t.count(t_set[j])

s_count.sort()
t_count.sort()

if s_count == t_count :
    print('Yes')
else :
    print('No')