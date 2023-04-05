N,M = map(int,input().split())

string = []

def dfs():
    if len(string) == M:
        print(' '.join(map(str,string)))
        return
    for i in range(1,N+1):
        if i not in string:
            string.append(i)
            dfs()
            string.pop()

dfs()

