N=input()
columns=N[0]
columns=(ord(columns)-ord('a'))+1
row=int(N[1])
direct=[[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
count=0
x=columns
y=row
for i in direct:
    columns+=i[0]
    row+=i[1]
    if(0<columns<9 and 0<row<9):
        count+=1
    columns=x
    row=y
print(count)