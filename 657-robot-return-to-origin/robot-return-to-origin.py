class Solution:
    def judgeCircle(self, moves: str) -> bool:
        updown = 0
        rightleft = 0

        for char in moves:
            if char == "U":
                updown += 1
            elif char == "D":
                updown -= 1
            elif char == "R":
                rightleft += 1
            elif char == "L":
                rightleft -= 1
            
        if updown == 0 and rightleft == 0:
            return True
        else:
            return False
    