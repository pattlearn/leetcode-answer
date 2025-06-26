class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        closet_sum = float("inf")
        closet_gap = float("inf")
        
        for i in range(len(nums) - 2):
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]
                
                if abs(current_sum - target) < closet_gap:
                    closet_gap = abs(current_sum - target)
                    closet_sum = current_sum
                    
                if current_sum > target:
                    R -= 1
                else:
                    L += 1
            
        return closet_sum