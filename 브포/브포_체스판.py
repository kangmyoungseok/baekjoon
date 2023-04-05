CHESSBOARD = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

def check_board(arr,i,j):
    diff = 0
    for row in range(8):
        for col in range(8):
            if arr[i+row][j+col] == CHESSBOARD[row][col]:
                diff+=1
    
    if diff > 32:
        return 64 - diff

    return diff

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(input())

min = 64
for i in range(N-7):
    for j in range(M-7):
        result = check_board(arr,i,j)
        if min > result:
            min = result

print(min)

