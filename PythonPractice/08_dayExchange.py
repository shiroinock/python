#!/usr/bin/python3
weeknumber = int(input('数(0-6)> '))
if weeknumber == 0 :
    print('日曜日')
elif weeknumber == 1 :
    print('月曜日')
elif weeknumber == 2 :
    print('火曜日')
elif weeknumber == 3 :
    print('水曜日')
elif weeknumber == 4 :
    print('木曜日')
elif weeknumber == 5 :
    print('金曜日')
elif weeknumber == 6 :
    print('土曜日')
else :
    print('0〜6までの整数を入力して下さい。')

# 0から6までの整数を入力して、それぞれ、0ならば「日曜」、1ならば「月曜」、...
# と結果を返すプログラムを書きなさい。
# 但し、0〜6の数以外の数値が入力された場合には、「0から6までの数を入力してください」と
# メッセージを返すようにしなさい。