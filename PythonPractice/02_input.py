#!/usr/bin/python3
eigo = int(input('英語の成績を入力して下さい> '))
sugaku = int(input('数学の成績を入力して下さい> '))
gokei = eigo + sugaku
heikin = gokei / 2
print('英語の得点:',eigo,sep=' ')
print('数学の得点:',sugaku,sep=' ')
print('合　　　計:',gokei,sep=' ')
print('平　　　均:',heikin,sep=' ')

# キーボードから英語と算数の成績を入力し、
# 入力された得点とともに、得点の合計と平均を計算して表示するプログラムを作成せよ。