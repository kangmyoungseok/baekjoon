import sys

input = sys.stdin.readline

N = int(input())
M = int(input())


arr = [[] for x in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

queue = []
bfs_visited = []

def bfs(s):
    queue.append(s)
    while queue:
        V = queue.pop(0)
        bfs_visited.append(V)
        for i in arr[V]:
            if (i not in bfs_visited) and (i not in queue):
                queue.append(i)
bfs(1)

print(len(bfs_visited)-1)
