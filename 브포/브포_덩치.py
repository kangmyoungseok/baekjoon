N = int(input())

WEIGHT = 0
HEIGHT = 1
RANK = 2

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(len(arr)):
    # 해당 인덱스보다 작은쪽 배열 탐색
    rank = 1
    me = arr[i]
    for bf in range(0,i):
        if me[WEIGHT] < arr[bf][WEIGHT] and me[HEIGHT] < arr[bf][HEIGHT]:
            rank +=1

    # 해당 인덱스보다 큰쪽 배열 탐색
    for af in range(i+1,len(arr)):
        if me[WEIGHT] < arr[af][WEIGHT] and me[HEIGHT] < arr[af][HEIGHT]:
            rank +=1
    arr[i].append(rank)

for man in arr:
    print(man[RANK])