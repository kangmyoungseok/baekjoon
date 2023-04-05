from collections import deque


N,K = map(int,input().split())

queue = deque([x for x in range(1,N+1)])

result = '<'
while True:
    try:
        for i in range(K-1):
            queue.append(queue[0])
            queue.popleft()
        result += str(queue.popleft()) + ', '
    except:
        break
result = result[:-2] + '>'
print(result)