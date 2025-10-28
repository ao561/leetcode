class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def tz(n):
            tz = 0
            i = 1

            while n >= 5**i:
                tz += (n//5**i)
                i += 1
            
            return tz

        def find_smallest_n(target_k):
            L, R = 0, 5*(10**9)
            ans = 0

            while L <= R:
                mid = (L+R) // 2
                zeros = tz(mid)

                if zeros >= target_k:
                    ans = mid
                    R = mid - 1
                else:
                    L = mid + 1
            
            return ans
        
        return find_smallest_n(k+1) - find_smallest_n(k)
        


        


        
        

