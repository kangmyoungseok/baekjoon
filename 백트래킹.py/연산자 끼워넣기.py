import sys

input = sys.stdin.readline

A = []
op = []

_ = input()

A = list(map(int,input().split()))
op = list(map(int,input().split()))

min_value = 1e9
max_value = -1e9

def dfs(depth,total,plus,minus,multi,div):
    global min_value
    global max_value
    if depth == len(A):
        if total < min_value: min_value = total
        if total > max_value: max_value = total
    if plus:
        dfs(depth+1,total+A[depth],plus-1,minus,multi,div )
    if minus:
        dfs(depth+1,total-A[depth],plus,minus-1,multi,div )
    if multi:
        dfs(depth+1,total*A[depth],plus,minus,multi-1,div )
    if div:
        dfs(depth+1,int(total/A[depth]),plus,minus,multi,div-1)

dfs(1,A[0],op[0],op[1],op[2],op[3])
print(max_value)
print(min_value)