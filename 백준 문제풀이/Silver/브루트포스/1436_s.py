n=int(input())

count=0
num=665
while True:
    num+=1
    if "666" in str(num):
        count+=1
    if n==count:
        break

print(num)