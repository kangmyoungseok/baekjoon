import sys

N = int(input())
arr = sys.stdin.readline().split()

arr = [int(a) for a in arr]

arr.sort()

M = int(input())
arr2 = sys.stdin.readline().split()
arr2 = [int(a) for a in arr2]

for a in arr2:
    # a가 arr에 있는지 이진 탐색을 통해서 검색한다.
    # arr은 sorting 되어있음
    start,end = 0,N-1
    is_found = False
    while start <= end:
        search = (start + end) // 2
        if a == arr[search]:
            is_found = True
            break
        elif a < arr[search]:
            end = search - 1
        else:
            start = search + 1
    if is_found == True:
        print(1)
    else:
        print(0)

 
