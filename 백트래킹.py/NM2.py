N,M = map(int,input().split())

s = []
def dfs(i):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for j in range(i+1,N+1):
        s.append(j)
        dfs(j)
        s.pop()

dfs(0)