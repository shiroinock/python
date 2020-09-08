K = int(input())
A, B = map(int, input().split())

MaxKx = B//K*K

if MaxKx >= A :
    print('OK')
else :
    print('NG')