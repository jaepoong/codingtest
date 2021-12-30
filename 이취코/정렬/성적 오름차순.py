N=int(input())
student=[]

for i in range(N):
    student.append(list(input().split()))

student=sorted(student,key=lambda student:int(student[1]))

print(student)