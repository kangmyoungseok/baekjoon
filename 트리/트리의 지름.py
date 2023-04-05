import sys

N = int(input())

tree = [[] for x in range(N+1)]

# tree 구성
for i in range(N):
    arr = list(map(int,sys.stdin.readline().split()))
    for i in range((len(arr)//2) -1 ):
        node = [arr[2*i+1],arr[2*i+2]]
        tree[arr[0]].append(node)

# dfs
# 1번 노드에서 가장 먼 노드를 찾고, 그 노드에서 가장 먼 노드와의 거리가 지름이다.

max_node = 0
max_dist = 0
visited = [0 for _ in range(N+1)]


def dfs(parent,dist):
    global max_node
    global max_dist
    for node in tree[parent]:
        if visited[node[0]] == 0 :
            dist_next = dist + node[1]
            visited[node[0]] = 1
            if dist_next > max_dist :
                max_node = node[0]
                max_dist = dist_next
            dfs(node[0],dist_next)
            
            
dfs(1,0)
max_dist = 0
visited = [0 for _ in range(N+1)]
visited[max_node] = 1
dfs(max_node,0)
print(max_dist)