from collections import deque
import sys

input = sys.stdin.readline


N = int(input())
queue = deque([])

for i in range(N):
    operations = input().split()
    op = operations[0]
    if op == 'push':
        queue.append(operations[1])
    elif op == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif op == 'size':
        print(len(queue))
    elif op == 'empty':
        if len(queue) == 0 :
            print(1)
        else:
            print(0)
    elif op == 'front':
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[0])
    elif op == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
