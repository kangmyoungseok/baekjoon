from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

queue = deque([x+1 for x in range(N)])
target = list(map(int,input().split()))

def queue_left(queue,target):
    count = 0
    while queue[0] != target:
        queue.append(queue.popleft())
        count +=1

    return count

def queue_right(queue,target):
    count = 0 
    while queue[0] != target:
        queue.appendleft(queue.pop())
        count+=1

    return count

total = 0
for i in target:
    cur_queue = queue.copy()
    left_count = queue_left(cur_queue,i)

    cur_queue = queue.copy()
    right_count = queue_right(cur_queue,i)

    if left_count <= right_count:
        queue_left(queue,i)
        total += left_count
    else:
        queue_right(queue,i)
        total += right_count
    queue.popleft()

print(total)
