n = int(input())
c=[]
nums = list(map(int,input().split()))
for i in range(n):
    c.append(nums[:i+1].count(nums[i]))
for i in range(n):
    print(c[i],end=' ')
