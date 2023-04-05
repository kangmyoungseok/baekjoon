import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

tree = [[] for i in range(N+1)]
parents = [0 for i in range(N+1)]
parents[1] = 1

for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def tree_dfs(parent):
    for node in tree[parent]:
        if parents[node] == 0:
            parents[node] = parent
            tree_dfs(node)

tree_dfs(1)

for i in range(2,N+1):
    print(parents[i])