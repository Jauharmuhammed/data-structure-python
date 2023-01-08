from collections import deque

queue_deque = deque()

queue_deque.appendleft(0)
queue_deque.appendleft(1)
queue_deque.appendleft(2)
queue_deque.appendleft(3)
queue_deque.appendleft(4)

print(queue_deque)

queue_deque.pop()
print(queue_deque)
