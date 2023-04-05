x,y,w,h = map(int,input().split())

case1 = x
case2 = w - x
case3 = y
case4 = h - y

print(min(case1,case2,case3,case4))
