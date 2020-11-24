n=int(input())
sum = 0
while n:
    sum+=int(n%10)
    n=n/10
    n=int(n)
print(sum)