N = int(input())

def calc(N):
    M = 4
    for i in range(N):
        M = M + 5 * ( 4 ** i) - 2 * (2**i) * (2**i - 1) 
    return M
print(calc(N))
