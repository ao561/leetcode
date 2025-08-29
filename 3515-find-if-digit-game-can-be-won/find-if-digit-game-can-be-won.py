class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singlesum = 0
        doublesum = 0

        for num in nums:
            if len(str(num)) == 2:
                doublesum += num
            elif len(str(num)) == 1:
                singlesum += num
        
        if singlesum == doublesum:
            return False
        else:
            return True
