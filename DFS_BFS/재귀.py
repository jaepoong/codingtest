def recursive_function(i):
    print(i,"번째재귀함수")
    i+=1
    if i==100:
        return
    recursive_function(i)
recursive_function(3)