import sys

input = sys.stdin.readline

N = int(input())
Arr = list(map(int,input().split()))

M = int(input())
Arr2 = list(map(int,input().split()))

card_dict = {}
for i in Arr:
    try:
        card_dict[i] += 1
    except KeyError:
        card_dict[i] = 1

for i in Arr2:
    try:
        print(card_dict[i],end=' ')
    except KeyError:
        print(0, end=' ')