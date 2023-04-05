while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a,b,c) == a:
        if pow(a,2) == pow(b,2) + pow(c,2):
            print('right')
            continue
    if max(a,b,c) == b:
        if pow(b,2) == pow(a,2) + pow(c,2):
            print('right')
            continue
    if max(a,b,c) == c:
        if pow(c,2) == pow(a,2) + pow(b,2):
            print('right')
            continue
    print('wrong')

