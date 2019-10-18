yohou = str(input())

yohou_list = list(yohou)

tenki = str(input())

tenki_list = list(tenki)

hi = 0

onaji = 0

while hi < 3 :
    if yohou_list[hi] == tenki_list[hi] :
        onaji+=1
    hi+=1

print(onaji)