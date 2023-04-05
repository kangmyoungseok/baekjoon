import sys

input = sys.stdin.readline

N = int(input())
M = int(input())


arr = [[] for x in range(N+1)]

for i in range(M):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

dfs_visited = []

def dfs(s):
    if s not in dfs_visited:
        dfs_visited.append(s)
    for i in arr[s]:
        if i not in dfs_visited:
            dfs(i)

dfs(1)
print(len(dfs_visited)-1)

