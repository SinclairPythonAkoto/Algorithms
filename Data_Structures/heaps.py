"""Heaps

Heaps are a tree-like data structure that satisifies the heap of the 
property, where each node is either greater (or smaller) than it's children,
used for effiecient implementation of priority queues and sorting algorithms.

A common use of a heap is to implement a priority queue, where elements are stored in the heap and retrieved in order of their priority. For example, you might use a heap to implement an event scheduler, where each event has a priority (e.g. a timestamp) and events are executed in order of their priority.

In this example, we use the heapq module from the Python standard library to implement a heap data structure. The PriorityQueue class provides methods for pushing elements onto the heap with a given priority, and popping the element with the highest priority. The heapq module uses a min-heap implementation, so we negate the priority value to get a max-heap.
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# create a queue
queue: PriorityQueue = PriorityQueue()
queue.push('item 1', 3)
queue.push('item 2', 2)
queue.push('item 3', 1)

print(queue.pop())
print(queue.pop())
print(queue.pop())


# Output
# item 1
# item 2
# item 3