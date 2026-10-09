class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        times = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        times = []
        for i in cars:
            time = (target-i[0])/i[1]
            times.append(time)
        stack = []
        for time in times:
            if not stack or stack[-1]<time:
                stack.append(time)
            
        return len(stack)