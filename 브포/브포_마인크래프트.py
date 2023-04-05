import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())

graph = []
max = 0
for i in range(N):
    graph.append(list(map(int,input().split())))


min_time = 1e9
max_height = 0
for height in range(257):
    low_block,high_block = 0,0
    for row in range(N):
        for col in range(M):
            if graph[row][col] <= height:
                low_block += height - graph[row][col]
            else:
                high_block += graph[row][col] - height
    
    if low_block > high_block + B:
        continue

    time = high_block*2 + low_block
    if min_time >= time:
        max_height = height
        min_time = time
    
print(f"{min_time} {max_height}")

 
    
