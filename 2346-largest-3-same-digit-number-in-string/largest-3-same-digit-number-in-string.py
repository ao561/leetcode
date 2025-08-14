class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = float('-inf')

        for i in range(len(num) - 2):
            substring = num[i:i+3]

            if substring[0] == substring[1] and substring[1] == substring[2] and int(substring) > maxi:
                maxi = int(substring)
        
        if maxi == float('-inf'):
            return ""
        elif maxi == 0:
            return "000"    
        else:   
            return str(maxi)