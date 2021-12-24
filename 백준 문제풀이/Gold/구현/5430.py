T=int(input())
condition=True
myr=[]
for j in range(T):
    function=input()
    n=int(input())
    li=input()
    li=li[1:-1]
    li=li.split(",")
    print(li)
    for i in function:
        if i=="R":
            li.reverse()
        if i=="D":
            if len(li)<1:
                condition=False
            else:
                li.pop()
    if condition==False:
        result="error"
    else:    
        result="["
        for i in li:
            result+=i
            result+=""
        result+="]"
    myr.append(result)
for i in myr:
    print(i)