n=input()
if n[0]=='-':
    n=int(n[1:])
    print("-1")
elif n[0]=="0":
    n=int(n)
    print("0")
else:
    n=int(n)
    print("1")

s = [0, 1]
for i in range(2, abs(n) + 1):
    s.append((s[i - 1] + s[i - 2]) % 1000000000)

print(s[n])
