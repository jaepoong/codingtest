N=int(input())
x=[]
for i in range(N):
    input_data=input().split()
    x.append((input_data[0],int(input_data[1])))
array=sorted(x,key=lambda student: student[1])
for i in range(len(array)):
    print(array[i][0], end=" ")