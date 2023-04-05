import sys


N = int(input())

info = []
for i in range(N):
    age,name = sys.stdin.readline().rstrip().split()
    age = int(age)
    info.append([age,name])

info.sort(key=lambda x:x[0])

for i in info:
    print(f"{i[0]} {i[1]}")