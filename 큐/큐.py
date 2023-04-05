from collections import deque
import sys

N = int(input())

queue = deque([])

for i in range(N):
    op = sys.stdin.readline().rstrip().split()
    if op[0] == 'push':
        queue.append(int(op[1]))
    elif op[0] == 'pop':
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    elif op[0] == 'front':
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    elif op[0] == 'back':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
        
