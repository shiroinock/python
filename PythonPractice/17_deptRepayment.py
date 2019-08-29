#!/usr/bin/python3
shakkin = int(input('借金> '))
riritsu = float(input('年利率(%)> '))
hensai =  int(input('返済額> '))
total = 0
month = 0
while shakkin > hensai :
    month += 1
    shakkin = shakkin*(1 + riritsu/12/100) - hensai
    print(str(month)+'月: 返済額',hensai,'円','残り',\
    int(shakkin),sep=' ')
    total += hensai
month += 1
shakkin = shakkin*(1 + riritsu/12/100)
total += shakkin
print(str(month)+'月: 返済額',int(shakkin),'円','これで完済。','返済総額: ',\
int(total),'円',sep=' ')

# 借金をして月々、定額を返済していくと借金はどうなっていくのかを調べるプログラムを作成しよう。
# 借金の金額と、利息の年利率(%)、月々の返済額を入力すると、
# 毎月、借金がなくなるまで月数と借金の金額を表示するものとする。
# 月々の借金は、借金の利息年利率/12（月割り）分増加するが、返済分だけ減る。