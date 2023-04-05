import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

'''
    A C A Y K P
  0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
P 0 1 1 2 2 2 3
C 0 1 2 2 2 2 3
A 0 1 2 3 3 3 3
K 0 1 2 3 3 4 4
'''

dp = [[0 for x in range(len(str1)+1)] for _ in range(len(str2)+1)]


for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])
