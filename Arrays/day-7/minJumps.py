def minJumps(arr, n):
	    maxReach=arr[0]
	    step=arr[0]
	    jump=1
	    if(n==1):
	        return 0
	    elif(arr[0]==0):
	        return -1
	    else:
	        for i in range(1,n):
	            if(i==n-1):
	                return jump
	            maxReach=max(maxReach, i+arr[i])
	            step=step-1
	            if(step==0):
	                jump=jump+1
	                if(i>=maxReach):
	                    return -1
	                step=maxReach-i
arr=list(map(int,input().split()))
n=len(arr)
result=minJumps(arr,n)
print(result)
