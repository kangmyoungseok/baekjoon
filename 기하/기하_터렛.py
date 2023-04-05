N = int(input())

def solve():
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 접점이 무한대인 경우
    if (x1,y1) == (x2,y2):
        if r1 == r2:
            print(-1)
            return
        else:
            print(0)
            return

    # 접점이 하나인 경우
    dist = (pow(x2-x1,2) + pow(y2-y1,2))**0.5
    if r1 + r2 == dist:
        print(1)
        return
    if max(r1,r2) - min(r1,r2) == dist:
        print(1)
        return

    # 접점이 2개인 경우
    # r1 + r2 가 dist 보다 크고, max(r1,r2) - min(r1,r2) < dist인 경우
    if r1 + r2 > dist and max(r1,r2) - min(r1,r2) < dist:
        print(2)
        return

    print(0)

for i in range(N):
    solve()