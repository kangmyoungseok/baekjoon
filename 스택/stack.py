import sys
from queue import Empty


N = int(input())


stack = []
for i in range(N):
    op = sys.stdin.readline().rstrip().split()
    if op[0] == 'push':
        stack.append(int(op[1]))
    elif op[0] == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif op[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    
    
