n, l = map(int, input().split())
vs, ds = map(int, input().split())

if n == 0 :
    if ds >= l :
        print(ds / vs)
    else :
        print('impossible')