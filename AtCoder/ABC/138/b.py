n = int(input())

bunbo = [int(e) for e in input().split()]

wa = 0
for i in bunbo :
    wa = wa + 1 / i

print (1/wa)