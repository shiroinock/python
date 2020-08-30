# input 入力を受け取る split 入力された文字列をスペースで分けて解釈 
# int integer整数 整数として解釈
# map ()内のものを、前の変数にそれぞれ割り当てる
D,T,S = map(int, input().split())

#T 時間 S 速さ の積が D 距離 を上回るかどうか？

# * 掛け算
if T * S >= D :
    print('Yes')
else :
    print('No')