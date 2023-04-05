import sys
input = sys.stdin.readline

N,M = map(int,input().split())

tree = list(map(int,input().split()))

start,end = 0,max(tree)
mid = 0

while start <= end:
    mid = (start + end ) // 2
    total = 0
    for t in tree:
        if t > mid:
            total += t - mid
    if total >= M:
        start = mid + 1 
    else:
        end = mid - 1
    
print(end)