class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for i in range(1, len(words)):
            x, y = sorted(res[-1]), sorted(words[i])

            if x != y:
                res.append(words[i])
        
        return res

