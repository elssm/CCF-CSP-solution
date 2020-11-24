m = input()
count=0
num = list(map(int,input().split()))

for i in range(int(m)-1):
    for j in range(i+1,int(m)):
        if num[i]-num[j]==1 or num[i]-num[j] == -1:
            count+=1
print(count)
