class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        new_s = s.lower()
        
        for i in range(len(new_s)-1):
            if new_s[i] != new_s[i+1]:
                count += 1
        
        return count 
