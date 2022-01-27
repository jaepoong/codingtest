n=input()
le=len(n)//2
left=0
right=0
for i in range(le):
    left+=int(n[i])
    right+=int(n[le+i])

if left==right:
    print("LUCKY")
else:
    print("READY")