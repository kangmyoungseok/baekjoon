import sys

N = int(input())
arr1 = sorted(map(int,sys.stdin.readline().split()))

M = int(input())
arr2 = map(int,sys.stdin.readline().split())


result_dic = {}
result = []
for a in arr2:
    if a in result_dic:
        result.append(result_dic[a])
        continue
    is_found = False
    low,high = 0, N-1
    while low <= high:
        mid = (low + high)//2
        if a == arr1[mid]:
            is_found = True
            count = 1
            # 좌우를 추가 탐색해서 몇개가 있는지 확인
            # 1. 왼쪽 탐색
            tmp_mid = mid
            while True:
                tmp_mid = tmp_mid -1
                if a == arr1[tmp_mid]:
                    count += 1
                else:
                    break

            # 2. 오른쪽 탐색 
            tmp_mid = mid
            while True:
                if tmp_mid == N-1:
                    break
                tmp_mid = tmp_mid + 1
                if a == arr1[tmp_mid]:
                    count +=1
                else:
                    break
            result_dic[a] = str(count)
            result.append(str(count))
            break
        
        elif a < arr1[mid]:
            high = mid -1
        else:
            low = mid + 1
    if is_found == False:
        result_dic[a] = '0'
        result.append('0')

print(' '.join(result))