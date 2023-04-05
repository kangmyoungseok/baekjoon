from collections import deque
import sys

input = sys.stdin.readline

'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
'''


def solve():
    operations = input().rstrip()
    n = int(input())
    if n == 0 :
        input()
        queue = deque([])
    else:
        arr = list(map(int,input().rstrip()[1:-1].split(',')))
        queue = deque(arr)

    convert = False
    error = False
    for a in operations:
        if convert:
            if a == 'R':
                convert = False
            if a == 'D':
                if len(queue) == 0:
                    error=True
                    break
                queue.pop()

        else:
            if a == 'R':
                convert = True
            if a == 'D':
                if len(queue) == 0:
                    error = True
                    break
                queue.popleft()
    if error:
        print('error')
    else:
        if convert:
            arr = list(queue)[::-1]
        else:
            arr = list(queue)
        print('[' + ','.join(map(str,arr)) +']')


T = int(input())
for i in range(T):
    solve()

