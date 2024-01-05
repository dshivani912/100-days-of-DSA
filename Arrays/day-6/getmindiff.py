def getMinDiff(arr,n,k):
    arr.sort()
    mini=arr[0]
    maxi=arr[n-1]
    res=maxi-mini
    for i in range(1,n):
        if(arr[i]<k):
            continue
        mini=min(arr[i]-k,arr[0]+k)
        maxi=max(arr[i-1]+k,arr[n-1]-k)
        res=min(res,maxi-mini)
    return res
a=list(map(int,input().split()))
n=len(a)
k=int(input())
ans=getMinDiff(a,n,k)
print(ans)
