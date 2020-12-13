n,k,t,x1,y1,x2,y2=map(int,input().split())
a=0
b=0
for i in range(n):
    num = list(map(int,input().split()))
    count=0
    flag=0
    flag1=0
    for j in range(t):
        if num[2*j]>=x1 and num[2*j]<=x2 and num[2*j+1]>=y1 and num[2*j+1]<=y2:
            flag=1 #判断是否在风险地区经过
            count+=1
            if count>=k:
                flag1=1 #判断是否在风险地区经过
        else:
            count=0
    if flag:
        a+=1
    if flag1:
        b+=1
print(a)
print(b)

