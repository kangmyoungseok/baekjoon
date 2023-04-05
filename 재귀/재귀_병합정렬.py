import sys

result_dic = {}
count = 1

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


memo = {
    1 : 0, 
    2 : 2, 
    3 : 5  
}


def mergeSortCount(n, msMemo):
    if n in msMemo:
        return msMemo[n]
    nthMemo = mergeSortCount(int(n/2), msMemo) + mergeSortCount(n-int(n/2), msMemo) + n
    memo[n] = nthMemo
    return nthMemo


if mergeSortCount(N, memo)<K:
    print(-1)
    quit()

def merge(arr,p,q,r):
    i = p
    j = q+1
    t = 0
    global count
    global K
    tmp = [0 for x in range(r-p+1)]
    while i <= q and j <=r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t +=1
            i +=1
        else:
            tmp[t] = arr[j]
            t +=1
            j +=1
    while i <=q:
        tmp[t] = arr[i]
        t +=1 
        i +=1
    while j <=r:
        tmp[t] = arr[j]
        t +=1
        j +=1
    i = p
    t = 0
    while i <= r:
        arr[i] = tmp[t]
        result_dic[count] = tmp[t]
        count +=1
        if count-1 == K:
            print(result_dic[K])
            exit()
        i +=1 
        t += 1

def merge_sort(arr,p,r):
    if p < r :
        q = int((p+r)//2)
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)





merge_sort(arr,0,len(arr)-1)
print(-1)
