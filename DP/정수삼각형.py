import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [[0 for x in range(N)] for x in range(N)]

dp[0][0] = arr[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j] + arr[i][j]
            continue
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]

print(max(dp[N-1]))
