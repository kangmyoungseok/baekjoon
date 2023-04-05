import sys

arrP = sys.stdin.readline().split('+')

# parsing
arr = []
for a in arrP:
    arrM = a.split('-')
    for b in arrM:
        arr.append(int(b))
        arr.append('-')
    arr.pop()
    arr.append('+')
arr.pop()

# calc
result = 0
min_state = False
for val in arr:
    if min_state == True:
        if val == '-' or val == '+':
            continue
        else:
            result -= val
    else:
        if val == '-': min_state = True
        elif val == '+': continue
        else: result += val


print(result)