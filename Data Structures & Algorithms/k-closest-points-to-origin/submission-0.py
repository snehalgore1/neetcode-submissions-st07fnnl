import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            # print(h)
            d = p[0]*p[0]+p[1]*p[1]
            # print(d)
            heapq.heappush(h,(-d,p))
            while len(h)>k:
                heapq.heappop(h)
            # print(h)
            
        res = []
        # print(h)
        for r in h:
            res.append(r[1])
        return res