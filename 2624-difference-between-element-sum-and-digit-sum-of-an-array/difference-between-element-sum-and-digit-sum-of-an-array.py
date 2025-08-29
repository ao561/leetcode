class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementsum = 0
        digitsum = 0

        for num in nums:
            elementsum += num
            string = str(num)
            for char in string:
                digitsum += int(char)
        
        return abs(elementsum - digitsum)

        

        