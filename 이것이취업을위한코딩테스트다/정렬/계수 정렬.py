array=[7,5,3,2,4,1,2]
count=[0]*(max(array)+1)
for i in array:
    count[i]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
