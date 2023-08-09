# Move all the negative elements to one side of the array 

a=[-1,3,-4,-5,3,-6,-7]
low=0
mid=0
while(mid<len(a)):
    if(a[mid]<0):
        temp=a[mid]
        a[mid]=a[low]
        a[low]=temp
        mid=mid+1
        low=low+1
    else:
        mid=mid+1
print(a)
