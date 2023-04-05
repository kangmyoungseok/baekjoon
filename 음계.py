arr = list(map(int,input().split()))

def solve():
    if arr[0] < arr[1]:
        for i in range(1,7):
            if arr[i] > arr[i+1]:
                print("mixed")
                return
        print("ascending")

    else:
        for i in range(1,7):
            if arr[i] < arr[i+1]:
                print("mixed")
                return
        print("descending")

solve()