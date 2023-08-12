def rotate( arr, n):
    temp=arr[0:n-1]
    del arr[0:n-1]
    for i in range(len(temp)):
        arr.append(temp[i])
    return arr
arr=list(map(int,input().split()))
rotate(arr,len(arr))
