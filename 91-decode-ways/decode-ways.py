class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev, cur = 1, 0 if s[0] == "0" else 1

        for i in range(2, n+1):
            tmp = 0

            one_digit = s[i-1:i]
            two_digit = s[i-2:i]

            if int(one_digit) >= 1:
                tmp += cur
            
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                tmp += prev

            prev, cur = cur, tmp
        return cur