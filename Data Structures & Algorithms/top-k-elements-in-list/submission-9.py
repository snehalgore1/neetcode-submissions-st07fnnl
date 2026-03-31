class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            print(num)
            if num not in hm:
                hm[num]=1
            else:
                hm[num]+=1
        hm = sorted(hm.items(), key=lambda item: item[1], reverse=True)
        hm = dict(hm)
        print(hm)
        l=[]
        count = 0
        for key,value in hm.items():
            if count<k:
                print("in for loop")
                l.append(key)
            else:
                break
            count+=1
        # print(l)
        return l