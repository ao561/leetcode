class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                roman += sym[i]
               
        return roman