N = int(input())

queens = [0 for _ in range(N)]

result = 0

# 말의 위치 타당성 검증
def is_possible(row,col):
    # row,col위치에 놓을 수 있는가?
    for i in range(row):
        # 같은 열 검증
        if queens[i] == col:
            return False
        
        # 왼쪽 대각선 검증
        if row - col == i - queens[i]:
            return False
        
        # 오른 대각선 검증
        if row + col == i + queens[i]:
            return False
    
    return True

def NqueensUtil(row):
    global result
    if row == N:
        result +=1
        return
    for col in range(N):
        if is_possible(row,col):
            queens[row] = col
            NqueensUtil(row+1)

NqueensUtil(0)
print(result)





