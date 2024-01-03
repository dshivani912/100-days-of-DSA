def sum_subarray(a):
   all_sums=[]
   for i in range(0,len(a)-1):
      for j in range(i+1,len(a)):
        all_sums.append(sum(a[i:j]))
   return max(all_sums)
a=list(map(int,input().split()))
result=sum_subarray(a)
print(result)
