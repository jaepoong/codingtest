k=int(input())
x=[]
for i in range(k):
    n,m=map(int,input().split())
    x.append(m-n)
for i in x:
    q=0
    while True:
        if i<=q*(q+1):
            break
        q+=1
    
    if i<=q**2:
        print(q*2-1)
    else:
        print(q*2)
