n=input()
half=len(n)//2
result=0
for i in range(half):
    result=result+int(n[i])-int(n[half+i])
if result:
    print("READY")
else:
    print("LUCKY")