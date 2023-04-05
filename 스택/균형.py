import sys

s = sys.stdin.readline().rstrip()

stack = []
idx = 0
cond = False
while s[0] != '.':
    if s[idx] == '[' or s[idx] == '(':
        stack.append(s[idx])
    elif s[idx] == ']':
        if len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        else:
            print('no')
            cond = True
    elif s[idx] == ')':
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else:
            print('no')
            cond = True
    elif s[idx] == '.' and idx!=0:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
        cond = True
    idx += 1

    
    if cond:
        s = sys.stdin.readline().rstrip()
        stack = []
        idx = 0
        cond = False
            
