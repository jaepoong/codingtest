import math
def solution(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i]=math.ceil((100-progresses[i])/speeds[i])
    answer = []
    max=progresses[0]
    result=0
    for i in range(len(progresses)):
        if max<progresses[i]:
            answer.append(result)
            max=progresses[i]
            result=1
            continue
        result+=1
    answer.append(result)

    
    return answer