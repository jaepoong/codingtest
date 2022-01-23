n=input()
ma=0
for i in range(len(n)):
    ma=max(ma+int(n[i]),ma*int(n[i]))
print(ma)