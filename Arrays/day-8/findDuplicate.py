def findDuplicate(nums):
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast= nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow= nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
#driver code
nums=list(map(int,input().split()))
result=findDuplicate(nums)
print(result)
          
