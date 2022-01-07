#입력
import sys
input=sys.stdin.readline

#순열,조합
from itertools import permutations,combinations
data=['a','b','c']
per=list(permutations(data,2))
com=list(combinations(data,2))

#collections
from collections import deque
data=deque(data)
data.appendleft("3")
data.popleft()
data.append("4")

#Counter
# 등장 횟수 세기
from collections import Counter
counter=Counter(data)
print(counter("a"))
print(dict(counter))

# 수학
import math
print(math.sqrt(4))
print(math.pi, math.e)
print(math.gcd(21,14)) #최대공약수