S = input()

ans = 0

if S == 'RRR':
    print(3)
elif 'RR' in S:
    print(2)
elif 'R' in S:
    print(1)
else :
    print(0)