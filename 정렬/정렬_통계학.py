import sys

N = int(input())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()


def avg(arr):
    sum = 0
    for i in arr:
        sum += i
    return round(sum / len(arr))

def mid(arr):
    return arr[len(arr)//2]

def most(arr):
    max_count = 0
    most_value_arr = []
    count = 1
    for i in range(len(arr)):
        try:
            bf = arr[i]
            af = arr[i+1]
            if bf != af:                  
                if count == max_count:
                    most_value_arr.append(arr[i])
                elif count > max_count:
                    most_value_arr.clear()
                    max_count = count
                    most_value_arr.append(arr[i])
                count = 0
            count +=1
        except:
            if count > max_count:
                most_value_arr.clear()
                most_value_arr.append(arr[i])
            elif count == max_count:
                most_value_arr.append(arr[i])
                
    if len(most_value_arr) > 1:
        return most_value_arr[1]
    else:
        return most_value_arr[0]


def arrRange(arr):
    return arr[-1] - arr[0]

print(avg(arr))
print(mid(arr))
print(most(arr))
print(arrRange(arr))

# 산술평균 
# 중앙값
# 최빈값
# 범위


