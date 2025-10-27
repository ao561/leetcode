class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        intervals.sort()
        minHeap = []
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(minHeap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[query] = minHeap[0][0]
            else:
                res[query] = -1

        return [res[q] for q in queries]

