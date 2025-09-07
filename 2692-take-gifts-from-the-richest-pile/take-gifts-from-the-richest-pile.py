class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-num for num in gifts]
        heapq.heapify(gifts)

        while k > 0:
            x = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(x)))
            k -= 1
        
        return -sum(gifts)
