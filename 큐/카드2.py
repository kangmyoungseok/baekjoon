from collections import deque

N = int(input())
arr = [x for x in range(N,0,-1)]

queue = deque(arr)

while True:
    try:
        a = queue.pop()
        a = queue.pop()
        queue.appendleft(a)
        
    except:
        print(a)
        break

