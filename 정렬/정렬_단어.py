#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

import sys
N = int(input())

arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x:(len(x)))

for i in arr:
    print(i)
