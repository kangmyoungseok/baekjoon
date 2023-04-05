import sys


N = int(sys.stdin.readline())

coor = []
for i in range(N):
    coor.append(list(map(int,sys.stdin.readline().split())))

coor.sort(key=lambda x:(x[0],x[1]))
# coor.sort(key=lambda x:(x[1],x[0])) y우선순위
for i in coor:
    print(f"{i[0]} {i[1]}")
