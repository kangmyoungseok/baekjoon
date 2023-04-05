import sys

T = int(input())

def solve():
    string = sys.stdin.readline().rstrip()
    stack = []
    try:
        for c in string:
            if c == '(':
                stack.append(0)
            else:
                stack.pop()
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")


for i in range(T):
    solve()