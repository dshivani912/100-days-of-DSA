#Reverse an array

def reverse_an_array(a):
    start=0;end=len(a)-1;
    while(start<=len(a)//2):
        a[start],a[end]=a[end],a[start]
        start=start+1
        end=end-1
    return a

a=[1,2,3,4,5]
ans=reverse_an_array(a)
print(a)

#time complexity is O(n) and space complexity is O(1)
