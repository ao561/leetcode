class Solution:
    def frequencySort(self, s: str) -> str:
        maxHeap = []
        ans = ""
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for key, val in hashmap.items():
            heapq.heappush(maxHeap, [-val, key])
        
        while len(maxHeap) > 0:
            x = heapq.heappop(maxHeap)
            ans += x[1] * -x[0]
        
        return ans
