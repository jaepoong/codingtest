x=input()
count=0
result=0
for i in range(len(x)):
    if x[i]=="(":
        count+=1
    
    if x[i]==")" and x[i-1]=="(":
        count-=1
        result+=count
    
    elif x[i]==")":
        result+=1
        count-=1

print(result)