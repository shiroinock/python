#!/usr/bin/python3
n = int(input('数> '))
for j in range(1,n+1) :
    print(str(j)+':',end='') # 改行しない出力
    for i in range(0,j) :
        print('■',end='')
    print() # 改行だけ出力

# 数字を入力して、1からその数までの棒グラフを順に表示するプログラムを書きなさい。