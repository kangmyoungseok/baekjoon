import sys
input = sys.stdin.readline

N = int(input())
graph = []
visited = [False for i in range(N)]
for i in range(N):
    graph.append(list(map(int,input().split())))


min_diff = 1e9

def dfs(depth,idx):
    global min_diff
    if depth == N//2:
        start_score = 0
        link_score = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_score += graph[i][j]
                elif visited[i] == False and visited[j] == False:
                    link_score += graph[i][j]
        
        if abs(start_score - link_score) < min_diff:
            min_diff = abs(start_score - link_score)
        return
    
    for i in range(idx,N):
        visited[i] = True
        dfs(depth +1,i+1)
        visited[i] = False

dfs(0,0)
print(min_diff)

