#선입선출
from collections import deque
queue=deque()

queue.append(5)
queue.append(1)
queue.append(4)
queue.append(7)
queue.pop()
queue.popleft()
print(queue)