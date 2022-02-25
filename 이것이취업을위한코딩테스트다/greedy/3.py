n,m=map(int,input().split())
'''x=[]
for _ in range(n):
    x.append(list(map(int,input().split())))
k=[]
for i in range(n):
    k.append(min(x[i]))
print(max(k))'''
result=0
for i in range(n):
    data=map(int,input().split())
    min_a=min(data)
    result=max(result,min_a)
print(result)