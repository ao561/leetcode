class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) > 2:
            new_str = ""
            for i in range(len(s) - 1):
                new = str((int(s[i]) + int(s[i+1])) % 10)
                new_str += new
            s = new_str

        if s[0] == s[1]:
            return True
        else:
            return False
                
