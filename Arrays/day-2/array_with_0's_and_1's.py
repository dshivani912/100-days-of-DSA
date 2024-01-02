#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort_array_0s_1s_2s(A,n):  
  i=0  
  low = 0  
  mid = 0  
  high = n-1  
  while (mid<=high):  
    if (A[mid]==0):
      print("a[mid]==0")  
      print(mid,low,high)
      
      temp=A[mid]  
      A[mid]=A[low]  
      A[low]=temp  
      low = low + 1  
      mid = mid + 1
      print(A)
      
    elif (A[mid]==1):
      print("a[mid]==1")  
      print(mid,low,high)
      mid = mid + 1
      print(A)
    else:
      print("a[mid]==2")  
      print(mid,low,high)  
      temp=A[mid]  
      A[mid]=A[high]  
      A[high]=temp  
      high = high - 1
      print(A)
  
print("Enter size of an array: ")  
n=int(input())  
print("Enter array elements: \n")  
i=0  
A=[]  
while(i<n):  
  ele=int(input())  
  A.append(ele)  
  i=i+1  
print("Array after sorting: \n")  
sort_array_0s_1s_2s(A,n)  
i=0  
for i in A:  
  print(i) 



#Another method

a=[1,0,1,2,2,0]
for i in range(1,len(a)):
    while(a[i-1]>a[i] & i>=0):
        a[i-1],a[i]=a[i],a[i-1]
        print(a)
        i=i-1
print(a)
