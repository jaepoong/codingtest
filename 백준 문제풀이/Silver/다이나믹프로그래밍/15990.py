n=int(input())

array=[[0 for _ in range(3)] for i in range(100001)]
array[1]=[1,0,0]
array[2]=[0,1,0]
array[3]=[1,1,1]

for i in range(4,100001):
    array[i][0]=array[i-1][1]+array[i-1][2]
    array[i][1]=array[i-2][0]+array[i-2][2]
    array[i][2]=array[i-3][0]+array[i-3][1]


for i in range(n):
    x=int(input())
    print(sum(array[x])%1000000009)