import sys


while True:
    x,y = map(int,sys.stdin.readline().split())
    if (x,y) == (0,0):
        break
    if x > y :
        if x % y == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if y % x == 0:
            print("factor")
        else:
            print("neither")
    
    