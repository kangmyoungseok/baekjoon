import sys

input = sys.stdin.readline

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().rstrip())))

# 동 서 남 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = []
cnt = []
def bfs(i,j):
    queue.clear()
    queue.append([i,j])
    count = 1
    graph[i][j] = 0
    while queue:
        x,y = queue.pop(0)
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                count += 1
                queue.append([nx,ny])
                graph[nx][ny] = 0

    return count



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i,j))


cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)