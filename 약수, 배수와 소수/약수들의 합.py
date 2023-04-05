N = int(input())

result = []
def com_divisor(N):
    result.append(1)
    for i in range(2, int(N**(0.5)) +1 ):
        if N % i == 0 :
            result.append(i)
            result.append(N//i)
    result.sort()

def print_result(N):
    sum = 0
    for i in result:
        sum += i
    if sum == N:
        print(f'{N} = ', end='')
        print(' + '.join(map(str,result)))         
    else:
        print(f'{N} is NOT perfect.')

while N != -1:
    com_divisor(N)
    print_result(N)
    result = []
    N = int(input())


