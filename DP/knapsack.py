import sys
input = sys.stdin.readline

N,W = map(int,input().split())
backpack = []

for i in range(N):
    backpack.append(list(map(int,input().split())))

'''
   0 1 2 3 4 5 6 7 8 9 10
   0 0 0 0 0 0 0 0 0 0 0 
1  0 0 0 6 6 6 6 6   6   6   6
2  0 0 0 6 7 7 7 13 13  13  13
3  0 0 0 6 8 8 8 14 14  14  14
4  0 0 0 6 8 ..
5
6

'''


backpack.sort(key= lambda x:x[0])
dp = [[0 for weight in range(W+1)] for n in range(N+1)]

for i in range(1,N+1):
    for j in range(1, W+1):
        weight = backpack[i-1][0]
        price = backpack[i-1][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j-weight] +price,dp[i-1][j])
        



print(dp[N][W])
