from collections import deque
import sys

queue = deque([])
N = int(input())
for i in range(N):
    op = sys.stdin.readline().rstrip().split()
    if op[0] == 'push_front':
        queue.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        queue.append(int(op[1]))
    elif op[0] == 'pop_front':
        if len(queue) == 0 : print(-1)
        else: print(queue.popleft())
    elif op[0] == 'pop_back':
        if len(queue) == 0 : print(-1)
        else: print(queue.pop())
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0 : print(1)
        else: print(0)
    elif op[0] == 'front':
        if len(queue) == 0 : print(-1)
        else: print(queue[0])
    elif op[0] == 'back':
        if len(queue) == 0 : print(-1)
        else: print(queue[-1])


# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back