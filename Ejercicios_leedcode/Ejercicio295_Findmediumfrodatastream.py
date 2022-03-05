class MedianFinder:
    import heapq
    #Esto es un two heaps con la libreria de heaps
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap  or -self.max_heap[0] > num:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)       
            
        if len(self.max_heap) > len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
            
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2
        return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()