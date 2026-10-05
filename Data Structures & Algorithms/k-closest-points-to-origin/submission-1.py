class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_points = []
        for c in points:
            d= c[0]**2+c[1]**2
            distance_points.append([d,c])
        heapq.heapify(distance_points)
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(distance_points)[1])
        return ans