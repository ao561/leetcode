class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        level = []
        ans = 0

        for row in bank:
            count = 0
            if "1" in row:
                for num in row:
                    if num == "1":
                        count += 1
                level.append(count)

        for i in range(len(level) - 1):
            ans += level[i] * level[i+1]
        
        return ans 
