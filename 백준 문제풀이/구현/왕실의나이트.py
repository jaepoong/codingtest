space=input()
space=[int(ord(space[0]))-int(ord(space('a')))+1,space[1]]

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]

result=0
for i in range(8):
    dx_i=dx[i]
    dy_i=dy[i]
    
    space_i=[space[0]+dx_i,space[1]+dx_y]
    
    if space_i[0]<1 or space_i[0]<8 or space_i[1]<1 or space_i[1] > 8:
        continue
    result+=1
    