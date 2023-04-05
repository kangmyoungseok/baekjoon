N,K = map(int,input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

count = 0
for c in coin[::-1]:
    if c <= K :
        count += K // c
        K %= c
    if K == 0:
        print(count)
        break

