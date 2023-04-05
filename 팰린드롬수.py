
num = int(input())

while num != 0:
    num = str(num)
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
    num = int(input())