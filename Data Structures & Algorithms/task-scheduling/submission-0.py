from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        # Example: tasks = ["A","A","A","B","B","B"]
        # count = {"A": 3, "B": 3}
        count = Counter(tasks)

        # Step 2: Create a max heap
        # Python only supports min heap
        # Therefore we store negative frequencies

        maxheap = []

        for freq in count.values():
            heapq.heappush(maxheap, -freq)

        # Example:
        # maxheap = [-3,-3]

        # Step 3: Create a queue for tasks in cooldown
        # Each element stores:
        # (remaining_frequency, next_available_time)

        q = deque()
        
        # Step 4: Initialize time
        time = 0

        # Step 5: Continue until all tasks are completed
        # Both heap and queue must be empty

        while maxheap or q:

            # Move time forward by 1 unit
            time += 1

            # Step 6: Check if any task has completed cooldown
            # If its available time matches the current time,
            # move it back into the maxheap

            while q and q[0][1]==time:
                freq, available_time = q.popleft()
                heapq.heappush(maxheap,freq)

            # Step 7: Execute the most frequent available task
            if maxheap:
                freq = heapq.heappop(maxheap)

                # Since frequencies are negative,
                # adding 1 means one execution is completed

                # Example: -3 -> -2 -> -1 -> 0

                freq += 1

                # Step 8: Calculate when this task can execute again

                next_available_time = time + n + 1

                # Step 9: If the task still has remaining executions
                # add it to the cooldown queue

                if freq<0:
                    q.append((freq, next_available_time))

        # Step 10: Return total execution time
        return time