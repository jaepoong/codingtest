n=int(input())
array=[0 for _ in range(1000001)]
array[1]=1
array[2]=2
array[3]=4
array[4]=7

for i in range(5,1000001):
    array[i]=array[i-1]%1000000009+array[i-2]%1000000009+array[i-3]%1000000009

for i in range(n):
    x=int(input())
    print(array[x]%1000000009)