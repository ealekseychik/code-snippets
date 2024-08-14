# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self._insert_heap(val)
        elif val > self.heap[0]:
            self._replace_heap(val)
        
        return self.heap[0]

    def _insert_heap(self, val: int):
        self.heap.append(val)
        self.heap.sort()
    
    def _replace_heap(self, val: int):
        self.heap[0] = val
        self.heap.sort()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
