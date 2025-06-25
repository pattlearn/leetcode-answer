class Solution:
    def maxArea(self, height: list[int]) -> int:
        L = 0
        R = len(height) - 1
        max_vol = 0
        
        while L < R:
            w = R - L
            vol = w * min(height[L], height[R])
            
            if vol > max_vol:
                max_vol = vol
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return max_vol