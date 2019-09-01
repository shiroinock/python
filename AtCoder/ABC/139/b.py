""" a, b = map(int, input().split())

count = 1 

kuchi = a

while kuchi < b :
    count+=1
    kuchi = (a - 1) * count + 1
else :
    print(count) """