import sys

input = sys.stdin.readline

N,M = map(int,input().split())

miro = []
for i in range(N):
    miro.append(list(map(int,input().rstrip())))

# 동,서,남,북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = []
def bfs():
    queue.append([0,0])
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx > -1 and nx < N and ny > -1 and ny < M:
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append([nx,ny])
bfs()
print(miro[N-1][M-1])