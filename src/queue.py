#Queue using list and deque
from collections import deque
import array as arr

a = arr.array('d', [1.1, 7.8, 9,7])
print(a)

queue = deque(["Shrinish", "Heramb", "Ninad", "Shreyash"])

print(queue)
queue.append("Shriya")

print(queue)
queue.append("Vedashri")

print(queue)
print(queue.popleft())

queue = ["Shrinish", "Donde", "Heramb"]
queue.append("Shrinish")
queue.append("Donde")

print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)

