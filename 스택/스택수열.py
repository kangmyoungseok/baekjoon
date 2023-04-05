import sys

n = int(input())
current_val = 1
stack = []
result = ''
for _ in range(n):
    num = int(sys.stdin.readline())
    while num >= current_val:
        stack.append(current_val)
        result +='+'
        current_val += 1
    if num < current_val:
        if num == stack[-1]:
            stack.pop()
            result +='-'
        else:
            print('NO')
            sys.exit()

for i in result:
    print(i)

    

