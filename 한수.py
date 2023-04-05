def hansu(N):
    # 정수를 자리수의 숫자들로 분해
    if N < 100:
        return True

    units = N % 10
    tens = ( N // 10 ) % 10
    diff = units - tens

    N = N // 10
    while N >= 10:
        units = N % 10
        tens = (N // 10) % 10
        if diff != units - tens:
            return False
        N = N // 10

    return True

N = int(input())
count = 0
for i in range(1, N+1):
    if hansu(i) == True:
        count += 1

print(count)
