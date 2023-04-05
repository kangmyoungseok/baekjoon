def hanoi(arr,n,start,end):
    if n == 1: arr.append([start,end])
    else: 
        # n-1개를 start,end를 제외한 곳에 옮기기
        hanoi(arr,n-1,start,6-start-end)
        # n번째 원판은 start -> end로 옮기기
        arr.append([start,end])
        # n-1개를 start,end 제외한 곳에서 -> end로 옮기기
        hanoi(arr,n-1,6-start-end,end)

N = int(input())
arr = []
hanoi(arr,N,1,3)

count = 2**N -1
print(count)
for i,j in arr:
    print(f"{i} {j}")