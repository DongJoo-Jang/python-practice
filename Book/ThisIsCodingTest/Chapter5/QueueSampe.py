from collections import deque

queue = deque()

print(queue.append(5))
queue.append(2)
queue.append(3)
queue.append(7)
print(queue.popleft())
queue.append(1)
queue.append(4)
print(queue.popleft())

print(queue)
queue.reverse()
print(queue)
