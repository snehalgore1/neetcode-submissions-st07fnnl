class Solution:

    def encode(self, strs: List[str]) -> str:
        list2=[]
        s=""
        for i in range(0,len(strs)):
            l = len(strs[i])
            s = s+str(l)+'#'+strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        l = []
        num = []
        # print(s)
        j=0
        i=0
        while i<len(s):
            # print(i,s[i])
            if s[i] == "#":
                # print(s[j:i])
                length = int(s[j:i])
                # print(length)
                # print(s[(i+1):(i+length+1)])
                l.append(s[(i+1):(i+length+1)])
                i=i+length
                # print("i:",i)
                j=i+1
            i=i+1
            print(l)
        return l

                