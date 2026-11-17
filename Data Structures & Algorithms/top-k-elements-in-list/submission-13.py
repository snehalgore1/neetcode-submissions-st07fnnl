from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        m = len(nums)
        buckets = [0]*(m+1)
        for key,value in count.items():
            if buckets[value] == 0:
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        ret = []
        for i in range(m,-1,-1):
            if buckets[i]!=0:
                ret.extend(buckets[i])

            if len(ret)==k:
                return ret