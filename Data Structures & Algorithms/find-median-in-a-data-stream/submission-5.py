class MedianFinder:

    def __init__(self):
        self.left =[]
        self.right = []
        self.length =0
    def addNum(self, num: int) -> None:
        if self.length ==0:
            self.left.append(-num)
            self.length+=1
            return
        elif self.length ==1:
            if num>-self.left[0]:
                self.right.append(num)
            else:
                self.right.append(-self.left.pop(0))
                self.left.append(-num)
            self.length+=1
            return
        lv = -self.left[0]
        rv=self.right[0]

        if num>=rv:
            heapq.heappush(self.right, num)
            if len(self.right)>(len(self.left)+1):
                heapq.heappush(self.left, -heapq.heappop(self.right))
        else:
            heapq.heappush(self.left, -num)
            if len(self.left)>(len(self.right)+1):
                heapq.heappush(self.right, -heapq.heappop(self.left))
        self.length+=1



    def findMedian(self) -> float:
        if self.length%2:
            return float(-self.left[0]) if len(self.left)>len(self.right) else float(self.right[0])
        return (-self.left[0]+self.right[0])/2


        ["MedianFinder", "addNum", "-1", "addNum", "-2", "findMedian", "addNum", "-3", "findMedian", "addNum", "-4", "findMedian", "addNum", "-5", "findMedian"]