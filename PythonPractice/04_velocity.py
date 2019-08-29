#!/usr/bin/python3
hspeed = float(input('時速(km/h)> '))
sspeed = hspeed*1000.0/60**2
print('秒速 = ',sspeed,'m/s',sep=' ')

# 時速を秒速に直しましょう。
# 時速をkm/hの単位で入力すると、秒速がm/sの単位で表示されるプログラムを書きなさい。