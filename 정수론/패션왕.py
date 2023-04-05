def solve():
    n = int(input())
    dic = {}
    for i in range(n):
        name, types = input().split()
        try:
            dic[types] += 1
        except:
            dic[types] = 1
    
    result = 1
    for key,value in dic.items():
        result = result * (value+1)
    
    print(result - 1)
 


T = int(input())

for i in range(T):
    solve()