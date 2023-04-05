import sys

N = int(input())

stack = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

result = 0
for i in stack:
    result += i

print(result)