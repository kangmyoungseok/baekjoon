W,H,X,Y,P = map(int,input().split())

def in_circle(x1,y1,c1,c2,r):
    if pow(x1-c1,2) + pow(y1-c2,2) <= pow(r,2):
        return True
    return False

def in_rectangle(x1,y1,w,h,x,y):
    if x1 >= x and x1 <= x + w and y1 >= y and y1 <= y +h:
        return True
    return False

def solve():
    result = 0
    x1,y1 = map(int,input().split())
    if in_circle(x1,y1,X,Y+H/2,H/2) or in_circle(x1,y1,X+W,Y+H/2,H/2) or in_rectangle(x1,y1,W,H,X,Y):
        result =1
    return result
    

count = 0
for i in range(P):
    count += solve()

print(count)