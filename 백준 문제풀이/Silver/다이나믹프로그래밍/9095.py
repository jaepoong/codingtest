n=int(input())
array=[0]*12
array[1]=1
array[2]=2
array[3]=4
for i in range(4,12):
    array[i]=array[i-1]+array[i-2]+array[i-3]

for i in range(n):
    x=int(input())
    print(array[x])
