
def max_min(a):
    mini=a[0]
    maxi=a[0]

    for i in range(1,len(a)):
        if a[i]>maxi:
            maxi=a[i]
        elif (a[i]<mini):
            mini=a[i]
    return mini,maxi
        
a=[1,2,3,4,5]
print(max_min(a))



