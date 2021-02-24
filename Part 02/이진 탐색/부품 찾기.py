def binary_serach(array,target,start,end):
    if start > end:
        return None

    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_serach(array,target,start,mid-1)
    else:
        return binary_serach(array,target,mid+1,end)

N = int(input())

store = list(map(int,input().split()))
store.sort()

M = int(input())
consumer = list(map(int,input().split()))


for i in consumer:
    x = binary_serach(store, i, 0, N - 1)
    if x is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')