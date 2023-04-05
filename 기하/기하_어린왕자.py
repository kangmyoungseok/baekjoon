def in_circle(x1,y1,c1,c2,r):
    if pow(r,2) < pow(c1-x1,2) + pow(c2-y1,2):
        return True
    return False

def solve():
    x1,y1,x2,y2 = map(int,input().split())
    N = int(input())
    circle = []
    for _ in range(N):
        circle.append(list(map(int,input().split())))
    
    count = 0
    for c in circle:
        start = in_circle(x1,y1,c[0],c[1],c[2])
        end = in_circle(x2,y2,c[0],c[1],c[2])
        if start == True and end == False or start == False and end == True:
            count += 1
    
    print(count)
        
T = int(input())

for i in range(T):
    solve()