nums = list(map(int,input().split()))
count = 0
last = 2
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
        last = 2
    elif nums[i]==2:
        count+=last
        last+=2
    else:
        break
print(count)

