n=int(input())
for i in range(n):
    x=list(input().split())
    for j in x:
        print(j[::-1],end=" ")