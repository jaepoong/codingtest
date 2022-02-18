n=int(input())
for i in range(n):
    count=0
    result=0
    x=input()
    for j in x:
        if j=="(":
            count+=1
        else:
            count-=1
        
        if count==-1:
            result+=1
            break
    
    if not result and count==0:
        print("YES")
    else:
        print("NO")
    