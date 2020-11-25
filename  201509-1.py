n = int(input())
count=1
nums = list(map(int,input().split()))
for i in range(1,n):
    if nums[i]==nums[i-1]:
        continue
    else:
        count+=1
print(count)