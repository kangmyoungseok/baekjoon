N = int(input())

room = []
for i in range(N):
    start,end = map(int,input().split())
    room.append([start,end])

room.sort(key=lambda x: x[0])
room.sort(key=lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, N):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)