#1,2だけ合うクソコード

n = int(input())

for i in range(n):
    ketaume = '0'+str(n)+'b'
    print(format(i, ketaume).translate(str.maketrans({'0': 'a', '1': 'b'})))