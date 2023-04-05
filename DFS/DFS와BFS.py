import sys

input = sys.stdin.readline

N,M,S = map(int,input().split())
arr = [[] for x in range(N+1)]

for i in range(M):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(len(arr)):
    arr[i].sort()

dfs_visited = []
bfs_visited = []
queue = []

def dfs(s):
    if s not in dfs_visited:
        dfs_visited.append(s)
    else:
        return
    if len(dfs_visited) == N:
        return
    for i in arr[s]:
        dfs(i)

def bfs(s):
    queue.append(s)
    while queue:
        V = queue.pop(0)
        bfs_visited.append(V)
        for i in arr[V]:
            if (i not in bfs_visited) and (i not in queue):
                queue.append(i)

dfs(S)
bfs(S)

print(' '.join(map(str,dfs_visited)))
print(' '.join(map(str,bfs_visited)))
