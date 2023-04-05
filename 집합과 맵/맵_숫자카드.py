import sys

N = int(input())
sang_card = list(map(int,sys.stdin.readline().split()))

exists = {}
for i in sang_card:
    exists[i] = 1

M = int(input())
card_space = list(map(int,sys.stdin.readline().split()))

result = ''
for card in card_space:
    try:
        exists[card]
        result +='1 '
    except:
        result +='0 '

print(result)
