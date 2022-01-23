n=input()
x=int(n[0])
a,b=0,0
if x==0:
    a+=1
else:
    b+=1
for i in range(len(n)):
    num=int(n[i])
    if x !=num:
        if x == 0:
            a+=1
            x=num
        else:
            b+=1
            x=num

print(min(a,b))
    