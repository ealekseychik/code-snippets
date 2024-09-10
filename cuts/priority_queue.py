# Priority queue implementation in Python using heapq
# Avaliable methods are: 
# def Enqueue(obj: Object, priority: int) -> None
# def Dequeue() -> Object
# The bigger the priority number, the higher the priority
# On the same priority will be used FIFO

import heapq
from typing import Any

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    def Enqueue(self, obj: Any, priority: int) -> None:
        heapq.heappush(self.queue, (-priority, self.counter, obj))
        self.counter += 1

    def Dequeue(self) -> Any:
        if len(self.queue) == 0:
            return None
        return heapq.heappop(self.queue)[2]
    

class PriorityQueue2:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def __findHighestPriority(self):
        highest = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[highest][0] or \
                (self.queue[i][0] == self.queue[highest][0] and \
                    self.queue[i][1] < self.queue[highest][1]):
                highest = i
        return highest

    def Enqueue(self, obj: Any, priority: int) -> None:
        self.queue.append((priority, self.counter, obj))
        self.counter += 1

    def Dequeue(self) -> Any:
        if len(self.queue) == 0:
            return None

        highest = self.__findHighestPriority()
        _, _, obj = self.queue.pop(highest)
        return obj
