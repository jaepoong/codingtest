k=int(input())
x=[]
for i in range(k):
    a=int(input())
    if a==0:
        x.pop()
    else:
        x.append(a)

print(sum(x))        