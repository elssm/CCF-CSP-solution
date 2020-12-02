#这个题很奇怪，使用了append函数之后会显示超时，
#最后只能得30分到60分左右
#使用字典添加之后并对字典的key进行判断，最后AC

n,a,b = map(int,input().split())
num1=[]
num2=[]
dict1={}
dict2={}
sum = 0
for i in range(a):
    num1 = list(map(int,input().split()))
    dict1[num1[0]]=num1[1]
for j in range(b):
    num2 = list(map(int,input().split()))
    dict2[num2[0]] = num2[1]
for k in dict1.keys():
    if k in dict2.keys():
        sum+=(dict1[k] * dict2[k])
print(sum)