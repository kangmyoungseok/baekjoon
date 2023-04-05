from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

def solve():
    N,M = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    idx = deque([0 for x in range(len(queue))])
    idx[M] = 'target'
    count = 0
    while True:
        if queue[0] != max(queue):
            queue.append(queue.popleft())
            idx.append(idx.popleft())
        else:
            if idx[0] == 'target':
                print(count+1)
                break
            else:
                queue.popleft()
                idx.popleft()
                count +=1

    




for i in range(T):
    solve()