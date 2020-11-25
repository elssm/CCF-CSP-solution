price = int(input())
m = int(price / 50)
shengyu = price - m * 50
n = int(shengyu / 30)
yu = shengyu - n * 30
num = m*7 + n*4 + int(yu/10)
print(num)


