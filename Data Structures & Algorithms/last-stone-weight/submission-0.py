class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for x in stones:
            s.append(-x)
        
        heapq.heapify(s)
        
        while(len(s)>1):
            x = -s[0]
            heapq.heappop(s)
            y = -s[0]
            heapq.heappop(s)
            # print(x,y)
            diff = x-y
            if diff!=0:
                heapq.heappush(s,-diff)
            
        if len(s)==0:
            return 0
        else:
            return -s[0]