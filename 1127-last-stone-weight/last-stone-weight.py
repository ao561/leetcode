class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if x == y:
                continue
            elif x != y:
                heapq.heappush(stones, -1 * (y-x))
        
        if len(stones) == 0:
            return 0
        else:
            return -1 * stones[0]