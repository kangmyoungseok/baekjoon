import sys

N,M = map(int,sys.stdin.readline().split())

# 듣
d = {}
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    d[name] = 0

# 보
result = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    try:
        d[name]
        result.append(name)
    except:
        pass

print(len(result))
result.sort()
for name in result:
    print(name)

