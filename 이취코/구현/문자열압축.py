n=input()
res=len(n)
for i in range(1,len(n)//2+1):
    compressed=""
    count=1
    prev=n[0:i]
    for j in range(i,len(n),i):
        
        if n[j:j+i]==prev:
            count+=1
        
        else:
            compressed+=str(count)+prev if count>=2 else prev
            prev=n[j:j+i]
            count=1
            
    compressed+=str(count)+prev if count >=2 else prev
    res=min(res,len(compressed))
print(res)
            
    
        